import tkinter as tk
from tkinter import ttk, filedialog
from typing import Text
import ds_messenger
import Profile
from pathlib import Path


class Body(tk.Frame):
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance
        self._draw()

    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])
        entry = self._contacts[index]
        if self._select_callback is not None:
            self._select_callback(entry)

    def insert_contact(self, contact: str):
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        try:
            if len(contact) > 25:
                entry = contact[:24] + "..."
            id = self.posts_tree.insert('', id, id, text=contact)
        except:
            pass

    def insert_user_message(self, message:str):
        self.entry_editor.config(state='normal')
        self.entry_editor.insert(tk.END, message + '\n', 'entry-right')
        self.entry_editor.see(tk.END)
        self.entry_editor.config(state='disabled')

    def insert_contact_message(self, message:str):
        self.entry_editor.config(state='normal')
        self.entry_editor.insert(tk.END, message + '\n', 'entry-left')
        self.entry_editor.see(tk.END)
        self.entry_editor.config(state='disabled')

    def get_text_entry(self) -> str:
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5)
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right')
        self.entry_editor.tag_configure('entry-left', justify='left')
        self.entry_editor.config(state='disabled', bg='black', fg='white', font=('Helvetica', 9), highlightbackground='white', highlightthickness=10)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    def __init__(self, root, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20, command=self.send_click)
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="ICS 32 Messenger")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        #self.password...
        self.password_label = tk.Label(frame, width=30, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30, show='*')
        self.password_entry.insert(tk.END, len(self.pwd) * '*')
        self.password_entry.pack()


    def apply(self):
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()


class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        if Path('save_file.dsu').is_file():
            profile = Profile.Profile()
            profile.load_profile('save_file.dsu')
            self.username = profile.username
            self.password = profile.password
            self.server = profile.server
            self.contacts = profile._contacts
            self.messages = profile.messages
        else:
            self.username = input("Please enter username: ")
            self.password = input("Please enter password: ")
            self.server = "168.235.86.101"
            self.contacts = []
            self.messages = None
        self.recipient = None
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        #self.direct_messenger = ... continue!
        self.direct_messenger = ds_messenger.DirectMessenger(self.server, self.username, self.password)

        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()
        # self.body.insert_contact("jjjccc") # adding one example student.
        # self.body.insert_contact("ILOVEKIMCHAEWON534912")
        # self.body.insert_contact("SenZekken")
        # load saved contacts
        if self.contacts != None:
            for contact in self.contacts:
                self.body.insert_contact(contact['entry'])
                

    def send_message(self):
        # You must implement this!
        store = self.body.get_text_entry()
        self.direct_messenger.send(store, self.recipient)
        self.publish(store)

    def add_contact(self):
        # You must implement this!
        # Hint: check how to use tk.simpledialog.askstring to retrieve
        # the name of the new contact, and then use one of the body
        # methods to add the contact to your contact list
        # CONTACTS
        contact = tk.simpledialog.askstring('Add contact', 'Please enter contact name:')
        self.body.insert_contact(contact)
        upload = Profile.Contact()
        upload.set_entry(contact)
        new_profile = Profile.Profile(self.server, self.username, self.password)
        # MESSAGES 
        try:
            messages = self.direct_messenger.retrieve_all()
            online = Profile.Message()
            online.set_entry(messages)
            try:
                new_profile._contacts = self.contacts
                new_profile.messages = self.messages
            except:
                pass
            new_profile.add_contact(upload)
            new_profile.add_message(online)
            new_profile.save_profile('save_file.dsu')
        except:
            print("Connection Error! Please connect to a stable internet connection.")
    
    def recipient_selected(self, recipient):
        self.recipient = recipient
        self.body.entry_editor.config(state='normal')
        self.body.entry_editor.delete(1.0, tk.END)
        self.body.entry_editor.config(state='disabled')
        new_profile = Profile.Profile(self.server, self.username, self.password)
        new_profile._contacts = self.contacts
        try: # wifi case
            store = self.direct_messenger.retrieve_all()
            online = Profile.Message()
            online.set_entry(store)
            for script in store:
                if self.recipient == script['from']:
                    self.body.insert_contact_message("  " + str(script['message']) + "\n")
            new_profile.add_message(online)
        except: # local case
            store = self.messages
            for script in store['entry']:
                if self.recipient == script['from']:
                    self.body.insert_contact_message("  " + str(script['message']) + "\n")
        new_profile.save_profile('save_file.dsu')


    def configure_server(self):
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.
        self.direct_messenger = ds_messenger.DirectMessenger(self.server, self.username, self.password)

    def publish(self, message:str):
        # You must implement this!
        self.body.entry_editor.config(state='normal')
        self.body.insert_user_message(message + "  \n")
        self.body.set_text_entry("")
        self.body.entry_editor.config(state='disabled')

    def check_new(self):
        # You must implement this!
        try:
            store = self.direct_messenger.retrieve_new()
            for script in store:
                if self.recipient == script['from']:
                    self.body.insert_contact_message("  " + str(script['message']) + "\n")
            self.root.after(3000, self.check_new)
        except:
            pass
    
    def new(self):
        filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Plain Text (*.txt)", "*.txt"), ("All Files (*.*)", "*.*")])
    
    def open(self):
        filedialog.askopenfilename()
    
    def close(self):
        main.destroy()
    
    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New File...', command=self.new)
        menu_file.add_command(label='Open File...', command=self.open)
        menu_file.add_command(label='Exit', command=self.close)

        settings_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact',
                                  command=self.add_contact)
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)

        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id = main.after(3000, app.check_new)
    print("ID:", id)
    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()

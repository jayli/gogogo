import rumps




class SimpleTrayApp(rumps.App):
    def __init__(self):
        super(SimpleTrayApp, self).__init__("Tray App",
                                            icon="./plane_fill.png",
                                            quit_button=None)
        self.menu = ['Item1', 'ChangeIcon', 'Quit']

    @rumps.clicked('Item1')
    def item1(self, _):
        rumps.alert("JK! No preferences available.")
        print("You clicked Item1")

    @rumps.clicked('ChangeIcon')
    def item2(self, _):
        rumps.Window("I can't think of a good example app...").run()
        self.icon = "./plant.png"
        print(self)

    @rumps.clicked('Quit')
    def quit(self, _):
        rumps.quit_application()

    @rumps.notifications
    def notification_center(self, info):
        print(info)

    def change_icon(self, _):
        print(_)
        if self.icon == "./plant.png":
            self.icon = "./plane_fill.png"
        else:
            self.icon = "./plant.png"


if __name__ == "__main__":
    app = SimpleTrayApp()
    timer = rumps.Timer(app.change_icon, 1)
    timer.start()
    app.run()

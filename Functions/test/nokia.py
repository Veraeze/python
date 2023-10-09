

def menu():
    menu_button = input("""
                   MENU 
            Press 1-> Phone Book
            Press 2-> Messages
            Press 3-> Chat
            Press 4-> Call Register
            Press 5-> Tones
            Press 6-> Settings
            Press 7-> Call Divert
            Press 8-> Games
            Press 9-> Calculator
            Press 10-> Reminders
            Press 11-> Clock
            Press 12-> Profiles
            Press 13-> SIM services
                """)

    match menu_button:
        case "1": phone_book()

        case "2": messages()

        case "3": print("Chat")

        case "4": call_register()

        case "5": tones()

        case "6": settings()

        case "7": print("Call Divert")

        case "8": print("Games")

        case "9": print("Calculator")

        case "10": print("Reminders")

        case "11": clock()

        case "12": print("Profiles")

        case "13": print("SIM services")

        case _:  menu()


def phone_book():
    button = input(""" 
                    Phone Book 
                Press 1 -> Search
                Press 2 -> Service Nos
                Press 3 -> Add name
                Press 4 -> Erase
                Press 5 -> Edit
                Press 6 -> Assign tone
                Press 7 -> Send b'card
                Press 8 -> Options
                Press 9 -> Speed dials
                Press 10 -> Voice tags
                Press 11-> back to main menu
                Press 
                """)
    match button:
        case "1": print("Search")

        case "2": print("Service Nos")

        case "3": print("Add name")

        case "4": print("Erase")

        case "5": print("Edit")

        case "6": print("Assign tone")

        case "7": print("Send b'card")

        case "8": options()

        case "9": print("Speed dials")

        case "10": print("Voice tags")

        case "12": menu()

        case _: phone_book()


def options():
    button = input("""
                    Options
                Press 1 -> Type of view
                Press 2 -> Memory status
                Press 3-> back
                Press 4-> main menu
                """)
    match button:
        case "1": print("Type of view")

        case "2": print("Memory status")

        case "3": phone_book()

        case "4": menu()

        case _: options()


def messages():
    button = input("""
                    Messages
                Press 1 -> Write messages
                Press 2-> Inbox
                Press 3 -> Outbox
                Press 4 -> Picture messages
                Press 5 -> Templates
                Press 6 -> Smileys
                Press 7 -> Message settings
                Press 8 -> Info service
                Press 9 -> Voice mailbox number
                Press 10 -> Service command editor
                Press 11-> back to main menu
                """)
    match button:
        case "1": print("Write messages")

        case "2": print("Inbox")

        case "3": print("Outbox")

        case "4": print("Picture messages")

        case "5": print("Templates")

        case "6": print("Smileys")

        case "7": message_settings()

        case "8": print("Info service")

        case "9": print("Voice mailbox number")

        case "10": print("Service command editor")

        case "11": menu()

        case _:  messages()


def message_settings():
    button = input("""
                Message Settings
                Press 1 -> Set 1
                Press 2 -> Common
                Press 3-> back
                Press 4-> main menu
                """)
    match button:
        case "1": set1()

        case "2": common()

        case "3": messages()

        case "4": menu()

        case _: message_settings()


def set1():
    button = input("""
                      Set 1
                Press 1 -> Message centre number
                Press 2 -> Message sent as
                Press 3 -> Message validity
                Press 4-> back
                Press 5-> previous
                Press 6-> main menu
                """)
    match button:
        case "1": print("Message centre number")

        case "2": print("Message sent as")

        case "3": print("Message validity")

        case "4": message_settings()

        case "5": messages()

        case "6": menu()

        case _: set1()


def common():
    button = input("""
                     Common
                Press 1 -> Deliver reports
                Press 2 -> Reply via same centre
                Press 3 -> Character support
                 Press 4-> back
                Press 5-> previous
                Press 6-> main menu
                """)
    match button:
        case "1": print("Deliver reports")

        case "2": print("Reply via same centre")

        case "3": print("Character support")

        case "4": message_settings()

        case "5": messages()

        case "6": menu()

        case _: common()


def call_register():
    button = input("""
                    Call Register
                Press 1 -> Missed calls
                Press 2 -> Received calls
                Press 3 -> Dialled numbers
                Press 4 -> Erase recent call lists
                Press 5 -> Show call duration
                Press 6 -> Show call costs
                Press 7 -> Call cost settings
                Press 8 -> Prepaid credit
                Press 9-> back to main menu
                """)
    match button:
        case "1": print("Missed calls")

        case "2": print("Received calls")

        case "3": print("Dialled numbers")

        case "4": print("Erase recent call lists")

        case "5": show_call_duration()

        case "6": show_call_costs()

        case "7": call_cost_settings()

        case "8": print("Prepaid credit")

        case "9": menu()

        case _: call_register()


def show_call_duration():
    button = input("""
                    Show Call Duration
                Press 1 -> Last call duration
                Press 2 -> All calls' duration
                Press 3 -> Received calls' duration
                Press 4 -> Dialled calls' duration
                Press 5 -> Clear timers
                Press 6-> back
                Press 7-> main menu
                """)
    match button:
        case "1": print("Last call duration")

        case "2": print("All calls' duration")

        case "3": print("Received calls' duration")

        case "4": print("Dialled calls' duration")

        case "5": print("Clear timers")

        case "6": call_register()

        case "7": menu()

        case _: show_call_duration()


def show_call_costs():
    button = input("""
                    Show Call Costs 
                Press 1 -> Last call cost
                Press 2 -> All calls' cost
                Press 3 -> Clear counters
                Press 4-> back
                Press 5-> main menu
                """)
    match button:
        case "1": print("Last call cost")

        case "2": print("All calls' cost")

        case "3": print("Clear counters")

        case "4": call_register()

        case "5": menu()

        case _: show_call_costs()


def call_cost_settings():
    button = input("""
                    Call Cost Settings
                Press 1 -> Call cost limit
                Press 2 -> Show costs in
                Press 3-> back
                Press 4-> main menu
                """)
    match button:
        case "1": print("Call cost limit")

        case "2": print("Show costs in")

        case "3": call_register()

        case "4": menu()

        case _: call_cost_settings()


def tones():
    button = input("""
                      Tones
                Press 1 -> Ringing tone
                Press 2 -> Ringing volume
                Press 3 -> Incoming call alert
                Press 4 -> Composer
                Press 5 -> Message alert tone
                Press 6 -> Keypad tones
                Press 7 -> Warning and game tones
                Press 8 -> Vibrating alert
                Press 9 -> Screen saver
                Press 10-> back to main menu
                """)
    match button:
        case "1": print("Ringing tone")

        case "2": print("Ringing volume")

        case "3": print("Incoming call alert")

        case "4": print("Composer")

        case "5": print("Message alert tone")

        case "6": print("Keypad tones")

        case "7": print("Warning and game tones")

        case "8": print("Vibrating alert")

        case "9": print("Screen saver")

        case "10": menu()

        case _: tones()


def settings():
    button = input("""
                    Settings
                Press 1 -> Call settings
                Press 2 -> Phone settings
                Press 3 -> Security settings
                Press 4 -> Restore factory settings
                Press 5-> back to main menu
                """)
    match button:
        case "1": call_settings()

        case "2": phone_settings()

        case "3": security_settings()

        case "4": print("Restore factory settings")

        case "5": menu()

        case _: settings()


def call_settings():
    button = input("""
                    Call Settings
                Press 1 -> Automatic redial
                Press 2 -> Speed dialling
                Press 3 -> Call waiting options
                Press 4 -> Own number sending
                Press 5 -> Phone line in use
                Press 6 -> Automatic answer
                Press 7-> back
                Press 8-> main menu
                """)
    match button:
        case "1": print("Automatic redial")

        case "2": print("Speed dialling")

        case "3": print("Call waiting options")

        case "4": print("Own number sending")

        case "5": print("Phone line in use")

        case "6": print("Automatic answer")

        case "7": settings()

        case "8": menu()

        case _: call_settings()


def phone_settings():
    button = input("""
                    Phone Settings
                Press 1 -> Language
                Press 2 -> Cell info display
                Press 3 -> Welcome note
                Press 4 -> Network selection
                Press 5 -> Lights
                Press 6 -> Confirm SIM service actions
                Press 7-> back
                Press 8-> main menu
                """)
    match button:
        case "1": print("Language")

        case "2": print("Cell info display")

        case "3": print("Welcome note")

        case "4": print("Network selection")

        case "5": print("Lights")

        case "6": print("Confirm SIM service actions")

        case "7": settings()

        case "8": menu()

        case _: phone_settings()


def security_settings():
    button = input("""
                    Security Settings 
                Press 1 -> PIN code request
                Press 2 -> Call barring service
                Press 3 -> Fixed dialing
                Press 4 -> Closed user group
                Press 5 -> Phone security
                Press 6 -> Change access codes
                Press 7-> back
                Press 8-> main menu
                
                """)
    match button:
        case "1": print("PIN code request")

        case "2": print("Call barring service")

        case "3": print("Fixed dialing")

        case "4": print("Closed user group")

        case "5": print("Phone security")

        case "6": print("Change access codes")

        case "7": settings()

        case "8": menu()

        case _: security_settings()


def clock():
    button = input("""
                      Clock 
                Press 1 -> Alarm clock
                Press 2 -> Clock settings
                Press 3 -> Date settings
                Press 4 -> Stopwatch
                Press 5 -> Countdown timer
                Press 6 -> Auto update of date and time
                Press 7 -> back to main menu
                """)
    match button:
        case "1": print("Alarm clock")

        case "2": print("Clock settings")

        case "3": print("Date settings")

        case "4": print("Stopwatch")

        case "5": print("Countdown timer")

        case "6": print("Auto update of date and time")

        case "7": menu()

        case _: clock()


if __name__ == "__main__":
    menu()

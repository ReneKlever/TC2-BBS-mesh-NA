import os
import sqlite3
import threading

thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, 'connection'):
        thread_local.connection = sqlite3.connect('bulletins.db')
    return thread_local.connection

def initialize_database():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bulletins (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    board TEXT NOT NULL,
                    sender_short_name TEXT NOT NULL,
                    date TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    content TEXT NOT NULL,
                    unique_id TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS mail (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT NOT NULL,
                    sender_short_name TEXT NOT NULL,
                    recipient TEXT NOT NULL,
                    date TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    content TEXT NOT NULL,
                    unique_id TEXT NOT NULL
                );''')
    c.execute('''CREATE TABLE IF NOT EXISTS channels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL
                );''')
    conn.commit()

def initialize_artikelen():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''DROP TABLE artikelen ''')
    c.execute('''CREATE TABLE artikelen (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naam TEXT NOT NULL,
                    omschrijving TEXT NOT NULL,
                    prijs NUMERIC(10,2) NOT NULL,
                    leverancier TEXT NOT NULL,
                    beschikbaar TEXT NOT NULL
                );''')
    conn.commit()

def initialize_bestellingen():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''DROP TABLE bestellingen ''')
    c.execute('''CREATE TABLE IF NOT EXISTS bestellingen (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_short_name TEXT NOT NULL,
                    klantnaam TEXT NOT NULL,
                    artikel INTEGER,
                    aantal INTEGER
                );''')
    conn.commit()

def list_bulletins():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, board, sender_short_name, date, subject, unique_id FROM bulletins")
    bulletins = c.fetchall()
    if bulletins:
        print_bold("Bulletins:")
        for bulletin in bulletins:
            print_bold(f"(ID: {bulletin[0]}, Board: {bulletin[1]}, Poster: {bulletin[2]}, Subject: {bulletin[4]})")
    else:
        print_bold("No bulletins found.")
    print_separator()
    return bulletins

def list_mail():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, sender, sender_short_name, recipient, date, subject, unique_id FROM mail")
    mail = c.fetchall()
    if mail:
        print_bold("Mail:")
        for mail in mail:
            print_bold(f"(ID: {mail[0]}, Sender: {mail[2]}, Recipient: {mail[3]}, Subject: {mail[5]})")
    else:
        print_bold("No mail found.")
    print_separator()
    return mail

def list_channels():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, url FROM channels")
    channels = c.fetchall()
    if channels:
        print_bold("Channels:")
        for channel in channels:
            print_bold(f"(ID: {channel[0]}, Name: {channel[1]}, URL: {channel[2]})")
    else:
        print_bold("No channels found.")
    print_separator()
    return channels

def list_artikelen():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, naam, omschrijving, prijs, leverancier, beschikbaar FROM artikelen")
    artikelen = c.fetchall()
    if artikelen:
        print_bold("Artikelen:")
        for artikel in artikelen:
            print_bold(f"(ID: {artikel[0]}, Naam: {artikel[1]}, Omschrijving: {artikel[2]}, Prijs: {artikel[3]}, Leverancier: {artikel[4]}, Beschikbaar: {artikel[5]})")
    else:
        print_bold("Geen artikelen gevonden.")
    print_separator()
    return artikelen

def list_bestellingen():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, sender_short_name, klantnaam, artikel, aantal FROM bestellingen")
    bestellingen = c.fetchall()
    if bestellingen:
        print_bold("Bestellingen:")
        for bestelling in bestellingen:
            print_bold(f"(ID: {bestelling[0]}, Sender: {bestelling[1]}, Klantnaam: {bestelling[2]}, Artikel: {bestelling[3]}, Aantal: {bestelling[4]})")
    else:
        print_bold("Geen bestellingen gevonden.")
    print_separator()
    return bestellingen

def ververs_artikelen():
    initialize_artikelen()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 100gr",3.00,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 200gr",3.50,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 300gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 400gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 500gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 600gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 700gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 800gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 900gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1000gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1100gr",3.99,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1200gr",3.99,"bas","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1300gr",3.50,"bas","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 4i1200gr",3.50,"bas","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1500gr",3.50,"kazan","ja"))
    c.execute(
        "INSERT INTO artikelen (naam, omschrijving, prijs, leverancier, beschikbaar) VALUES (?, ?, ?, ?, ?)",
        ("worst","bio runder 1600gr",3.50,"bas","ja"))
    conn.commit()

def delete_bulletin():
    bulletins = list_bulletins()
    if bulletins:
        bulletin_ids = input_bold("Enter the bulletin ID(s) to delete (comma-separated) or 'X' to cancel: ").split(',')
        if 'X' in [id.strip().upper() for id in bulletin_ids]:
            print_bold("Deletion cancelled.")
            print_separator()
            return
        conn = get_db_connection()
        c = conn.cursor()
        for bulletin_id in bulletin_ids:
            c.execute("DELETE FROM bulletins WHERE id = ?", (bulletin_id.strip(),))
        conn.commit()
        print_bold(f"Bulletin(s) with ID(s) {', '.join(bulletin_ids)} deleted.")
        print_separator()

def delete_mail():
    mail = list_mail()
    if mail:
        mail_ids = input_bold("Enter the mail ID(s) to delete (comma-separated) or 'X' to cancel: ").split(',')
        if 'X' in [id.strip().upper() for id in mail_ids]:
            print_bold("Deletion cancelled.")
            print_separator()
            return
        conn = get_db_connection()
        c = conn.cursor()
        for mail_id in mail_ids:
            c.execute("DELETE FROM mail WHERE id = ?", (mail_id.strip(),))
        conn.commit()
        print_bold(f"Mail with ID(s) {', '.join(mail_ids)} deleted.")
        print_separator()

def delete_channel():
    channels = list_channels()
    if channels:
        channel_ids = input_bold("Enter the channel ID(s) to delete (comma-separated) or 'X' to cancel: ").split(',')
        if 'X' in [id.strip().upper() for id in channel_ids]:
            print_bold("Deletion cancelled.")
            print_separator()
            return
        conn = get_db_connection()
        c = conn.cursor()
        for channel_id in channel_ids:
            c.execute("DELETE FROM channels WHERE id = ?", (channel_id.strip(),))
        conn.commit()
        print_bold(f"Channel(s) with ID(s) {', '.join(channel_ids)} deleted.")
        print_separator()

def display_menu():
    print("Menu:")
    print("1. List Bulletins")
    print("2. List Mail")
    print("3. List Channels")
    print("4. Delete Bulletins")
    print("5. Delete Mail")
    print("6. Delete Channels")
    print("7. List Artikelen")
    print("8. Ververs Artikelen")
    print("9. List Bestellingen")
    print("10. Verwijder alle Bestellingen")
    print("x. Exit")

def display_banner():
    banner = """
████████╗ ██████╗██████╗       ██████╗ ██████╗ ███████╗
╚══██╔══╝██╔════╝╚════██╗      ██╔══██╗██╔══██╗██╔════╝
   ██║   ██║      █████╔╝█████╗██████╔╝██████╔╝███████╗
   ██║   ██║     ██╔═══╝ ╚════╝██╔══██╗██╔══██╗╚════██║
   ██║   ╚██████╗███████╗      ██████╔╝██████╔╝███████║
   ╚═╝    ╚═════╝╚══════╝      ╚═════╝ ╚═════╝ ╚══════╝
Database Administrator
"""
    print_bold(banner)
    print_separator()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_bold(prompt):
    print("\033[1m")  # ANSI escape code for bold text
    response = input(prompt)
    print("\033[0m")  # ANSI escape code to reset text
    return response

def print_bold(message):
    print("\033[1m" + message + "\033[0m")  # Bold text

def print_separator():
    print_bold("========================")

def main():
    display_banner()
    initialize_database()
    while True:
        display_menu()
        choice = input_bold("Enter your choice: ")
        clear_screen()
        if choice == '1':
            list_bulletins()
        elif choice == '2':
            list_mail()
        elif choice == '3':
            list_channels()
        elif choice == '4':
            delete_bulletin()
        elif choice == '5':
            delete_mail()
        elif choice == '6':
            delete_channel()
        elif choice == '7':
            list_artikelen()
        elif choice == '8':
            ververs_artikelen()
        elif choice == '9':
            list_bestellingen()
        elif choice == '10':
            initialize_bestellingen()
        elif choice == 'x':
            break
        else:
            print_bold("Invalid choice. Please try again.")
            print_separator()

if __name__ == "__main__":
    main()

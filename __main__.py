import cmd
import MTGScrapping


def main():
    scrapper = MTGScrapping.web_scrapper()
    command = cmd.MTGCmd(scrapper)

    command.start()

if __name__ == '__main__':
    main()

import click

@click.command()
@click.option('--name', default='Test', help='Name of the participant.')
@click.version_option(version='1.1.0')
def main(name):
    """
    A demo App for BIOS259: The Art of Reproducible Science
    https://github.com/asntech/bios259-a24
    
    Author: Aziz Khan <azizk@stanford.edu>
    """

    print(f"Hello, {name}!\nWelcome to BIOS259 – The Art of Reproducible Science")

if __name__ == "__main__":
    main()

import click

from recipe.recipeMl import RecipeML


@click.group()
def main():
    """
    "This is a CLI"
    """
    pass

@click.command("orange")
@click.option('--state', '-s', default='start', help='start or stop')
def orange(state):
    if state is None:
        click.echo("missing state value")

    ml = RecipeML()

    ml.test()

    click.echo(state)


main.add_command(orange)

if __name__ == '__main__':
    main()
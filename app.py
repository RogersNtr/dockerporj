import click

@click.command()
def hello():
    click.echo('Hello the world!')
    
if __name__ =='__main__':
    hello()
# Calculator.py

import click



@click.command()
@click.argument('xs', type=int, nargs=-1)
def add(xs):
    '''
    Adds numbers.
    '''
    click.echo(sum(xs))


@click.command()
@click.argument('xs', type=int, nargs=-1)
def substract(xs):
    '''
    Substracts numbers.
    '''
    results = xs[0]
    for x in xs[1:]:
        results -= x
    click.echo(results)

# greeter.py
import click



@click.command()
@click.argument('first_name')
@click.option('--lang', help='Specify lan English (en) or Spanish (es)', default='en')
def greet(first_name, lang):
    '''
    Displays a greeting to the user.
    :name: Arguments
    :lang: Language
    '''
    if lang == 'es':
        greetings = 'Hola'
    elif lang == 'en':
        greetings = 'Hello'
    else:
        raise click.BadOptionUsage('lang', 'Unsupported Lang')
    click.echo(f' {greetings} {first_name}')

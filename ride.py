import os
import codecs
import subprocess
import click

from taxi import snapp


config = os.path.expanduser("~") + '/.config/snapp-cli/cook'
if not os.path.exists(config):
    os.mkdir(config)


def read_path():
    sp, dp = None, None
    path_file = open(config + 'path.csv', 'r')
    path = path_file.read()

    if path: 
        return [(float(i), float(j)) for i,j in [d.split(',') for d in path.split('\n')[:2]]]

    path_file.close()
    return sp, dp

sp, dp = read_path()


@click.group()
def cli():
    pass


@click.command()
@click.option('--username', '-u', type=str)
@click.option('--password', '-p', type=str)
def login(username, password):
    '''
    Login to your Snapp account
    '''
    ok = snapp.login(username=username, password=password)
    if ok:
        click.echo('Successful login.')


@click.command()
@click.option('--source', '-s', nargs=2, type=float)
@click.option('--destination', '-d', nargs=2, type=float)
@click.option('--map', '-m', is_flag=True)
def price(source, destination, map):
    '''
    Calculate price of a trip
    '''
    if map:
        subprocess.call(['mapscii'])
        source, destination = sp, dp
    else:
        pass
    
    r = snapp.ride(source[0], source[1], destination[0], destination[1])
    click.echo("\n======================\n")
    click.echo("Price: %d Rials\t Distance: %d" % r)
    click.echo("\n======================\n")


@click.command()
def ride():
    '''
    Compelete this function to take a ride with snapp

    Note: 
    - Use chrome or firefox
    - Please PEP8!!
    - Dynamic path file

    Your homework
    '''
    import time
    click.echo('Waiting...')
    time.sleep(5)
    click.echo('Find a driver')


cli.add_command(login)
cli.add_command(price)
cli.add_command(ride)


if __name__ == '__main__':
    cli()

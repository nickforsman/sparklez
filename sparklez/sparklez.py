#!/usr/bin/env python3
import click
import requests
import inquirer
from subprocess import call

npm_registry = "https://registry.npmjs.org/-/v1/search"
ruby_gems_repo = "https://rubygems.org/api/v1/search.json"

@click.command()
@click.option('--registry', default='npm', help='The registry to search from')
@click.argument('package')
def find(registry, package):
    """sparklez finds all packages for you and can even install them :O"""
    click.echo('sparklez is searching for your packages')
    if registry == 'npm':
        payload = {'text': package}
        r = requests.get(npm_registry, params=payload)
        responses = list(map(lambda a: a.get('package'), r.json().get('objects')))
        showPackages(responses, 'npm')
    elif registry == 'rubygems' or registry == 'ruby-gems':
        payload = {'query': package}
        responses = requests.get(ruby_gems_repo, params=payload).json()
        showPackages(responses, 'rubygems')
    else:
        click.echo(' ')
        click.echo('Registry {} is unknown to sparklez :S'.format(registry))

def showPackages(responses, reg):
    click.clear()
    try:
        if len(responses) > 0:
            responses = map(lambda response: response.get('name'), responses)
            questions = [
                inquirer.List(
                    'package',
                    message='These are the packges sparklez found',
                    choices=[*responses],
                ),
            ]
            answers = inquirer.prompt(questions)
            if answers != None:
                if reg == 'npm':
                    runCommand(['npm', 'install', answers.get('package')])
                elif reg == 'rubygems':
                    runCommand(['gem', 'install', answers.get('package'), '--user-install'])
        else:
            click.echo('sparklez couldn\'t find any packages that matched your search criteria')
    except KeyboardInterrupt:
        print('Goodbye!')

def runCommand(commands):
    click.echo('Running command: ' + ' '.join(commands))
    call(commands)

def main():
    find()

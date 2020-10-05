from invoke import task
import os

@task
def list_file_in_directory(c):
    c.run('ls -al')

@task
def run_all_tests(c):
    c.run('behave')

@task
def run_test_with_tag(c):
    '''
    In order to run this task from command line we can for example 
    do:
    TAGGED_TEST=@division invoke run-test-with-tag
    '''
    c.run('behave --tags={}'.format(os.environ['TAGGED_TEST']))

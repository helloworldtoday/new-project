import click
from search import run

@click.command()
@click.argument("username")
@click.option("--tor", is_flag=True, help="tor代理")
@click.option("--workers", default=5, help="執行緒數量")
def main(username, tor, workers):
    run(user_name=username, use_tor=tor, Max_workers=workers)

if __name__ == '__main__':
    main()

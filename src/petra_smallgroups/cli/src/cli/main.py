from sqlalchemy import text

from petra_smallgroups.data.src.data.assimilation import init_engine


def get_current_membership_applications() -> None:
    """
    Get all current membership applications from the database.
    """

    engine = init_engine()
    with engine.connect() as connection:
        result = connection.execute(text("select 'hello world'"))
        print(result.all())


if __name__ == "__main__":
    get_current_membership_applications()

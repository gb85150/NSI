import notion

def load_ical_into_notion(file, token, calendar_id):
    # load ical file into notion
    # file is the path to the ical file
    # returns the calendar id
    client = notion.NotionClient(token_v2=token)
    calendar = client.get_block(calendar_id)
    calendar.load_from_ical(file)
    return calendar.id

if __name__ == "__main__":
    load_ical_into_notion(file="calendar.ical", token="TOKEN", calendar_id="CALENDAR_ID")

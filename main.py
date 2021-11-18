def snap_message_sorter(from_user, to_user, descending):
    import json

    if from_user == "":
        exit("From whom do you want to view your chat history? Change it where main is called.")

    class SnapchatMessage:
        def __init__(self, user, created_date, message):
            self.user = user
            self.created_date = created_date
            self.message = message

    with open('chat_history/chat_history.json', 'r') as json_input:
        json = json.loads(json_input.read())

        received_messages = []
        sent_messages = []

        for received_message in json['Received Saved Chat History']:
            if received_message['From'] == from_user:
                received_messages.append(
                    SnapchatMessage(
                        received_message['From'],
                        received_message['Created'],
                        received_message['Text']
                    )
                )

        for sent_message in json['Sent Saved Chat History']:
            if sent_message['To'] == from_user:
                sent_messages.append(
                    SnapchatMessage(
                        to_user,
                        sent_message['Created'],
                        sent_message['Text']
                    )
                )

        joint_messages = (received_messages + sent_messages)

        sorted_list = sorted(joint_messages, key=lambda x: x.created_date, reverse=descending)

        for msg in sorted_list:
            print(msg.created_date)
            print(msg.user + ": ")
            print(msg.message + "\n")

if __name__ == '__main__':
    snap_message_sorter("", "me", descending=True)

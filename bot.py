# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Willkommen bei Stallings Capital!

Wir freuen uns, Sie als Teil unserer Community begrüßen zu dürfen! Bei Stallings Capital setzen wir uns dafür ein, jedem Mitglied zu helfen, sein Investmentwissen zu erweitern und finanziellen Erfolg zu erzielen. Egal, ob Sie ein erfahrener Investor sind oder gerade erst anfangen – hier finden Sie wertvolle Einblicke, Unterstützung und Möglichkeiten.

Zögern Sie nicht, Fragen zu stellen, Ideen zu teilen und an unseren Diskussionen teilzunehmen. Unser Team steht Ihnen zur Seite, und wir freuen uns darauf, gemeinsam mit Ihnen Ihre finanziellen Ziele zu erreichen!

Nochmals herzlich willkommen an Bord, und lassen Sie uns gemeinsam wachsen!

Mit freundlichen Grüßen,
Das Stallings Capital Team!")

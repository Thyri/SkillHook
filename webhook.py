import sys
import os
import hiscores
from discordWebhooks import Webhook, Attachment, Field

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


url = ""


def hook(username):
    applicant = hiscores.get_user_info(username)

    wh = Webhook(url, "Application for membership", username)

    at = Attachment(author_name=username, color="#ff0000", title="Skill Levels")

    field = Field("attack", applicant.attack, True)
    at.addField(field)
    field = Field("hitpoints", applicant.hitpoints, True)
    at.addField(field)
    field = Field("mining", applicant.mining, True)
    at.addField(field)
    field = Field("strength", applicant.strength, True)
    at.addField(field)
    field = Field("agility", applicant.agility, True)
    at.addField(field)
    field = Field("smithing", applicant.smithing, True)
    at.addField(field)
    field = Field("defence", applicant.defence, True)
    at.addField(field)
    field = Field("herblore", applicant.herblore, True)
    at.addField(field)
    field = Field("fishing", applicant.fishing, True)
    at.addField(field)
    field = Field("ranged", applicant.ranged, True)
    at.addField(field)
    field = Field("thieving", applicant.thieving, True)
    at.addField(field)
    field = Field("cooking :cooking:", applicant.cooking, True)
    at.addField(field)
    field = Field("prayer", applicant.prayer, True)
    at.addField(field)
    field = Field("crafting", applicant.crafting, True)
    at.addField(field)
    field = Field("firemaking", applicant.firemaking, True)
    at.addField(field)
    field = Field("magic", applicant.magic, True)
    at.addField(field)
    field = Field("fletching", applicant.fletching, True)
    at.addField(field)
    field = Field("woodcutting", applicant.woodcutting, True)
    at.addField(field)
    field = Field("runecrafting", applicant.runecrafting, True)
    at.addField(field)
    field = Field("slayer", applicant.slayer, True)
    at.addField(field)
    field = Field("farming", applicant.farming, True)
    at.addField(field)
    field = Field("construction", applicant.construction, True)
    at.addField(field)
    field = Field("hunter", applicant.hunter, True)
    at.addField(field)
    field = Field("total", applicant.total, True)
    at.addField(field)

    wh.addAttachment(at)

    wh.post()

    return

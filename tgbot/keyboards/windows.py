import operator

from aiogram.enums import ParseMode, ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Row,
    Select,
    SwitchTo,
    Column,
    Button,
    WebApp,
    Url,
)
from aiogram_dialog.widgets.media import StaticMedia, DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Text

from tgbot.keyboards.inline import (
    gate_1_inline,
    gate_2_inline,
    gate_3_inline,
    main_menu_inline,
    admin_panel_inline,
    add_menu_inline,
    menu_sections_inline,
    section_photo_inline,
    check_in_inline,
)
from tgbot.keyboards.reply import (
    gate_1_reply,
    gate_2_reply,
    gate_3_reply,
    main_menu_reply,
    admin_panel_reply,
    add_menu_reply,
    menu_sections_reply,
    check_in_reply,
)

from tgbot.keyboards.states import States

# from tgbot.keyboards.inline import main_menu_inline, choose_lang, links_list_inline, link_options_inline, \
#     option_action_inline, del_action_inline, add_link_inline
# from tgbot.keyboards.reply import choose_lang_reply, main_menu_reply, links_list_reply, new_link_reply, \
#     link_options_reply, del_action_reply
# from tgbot.keyboards.states import LinkBot


check_in_window = Window(
    DynamicMedia("gif_url"),
    Format("{title}"),
    Column(
        Select(
            Format("{item[0]}"),
            id="check_in",
            item_id_getter=operator.itemgetter(1),
            items="check_in_buttons",
            on_click=check_in_reply,
        ),
    ),
    parse_mode=ParseMode.HTML,
    state=States.check_in_state,
    getter=check_in_inline,
)


gate_window_1 = Window(
    StaticMedia(
        url="https://telegra.ph//file/16de46d2de57505dedfd1.jpg",
    ),
    Format("{gate_1_title}"),
    Column(
        Select(
            Format("{item[0]}"),
            id="gate_1",
            item_id_getter=operator.itemgetter(1),
            items="gate_1_buttons",
            on_click=gate_1_reply,
        ),
    ),
    parse_mode=ParseMode.HTML,
    state=States.gate_state_1,
    getter=gate_1_inline,
)


gate_window_2 = Window(
    Format("{gate_2_title}"),
    Column(
        Select(
            Format("{item[0]}"),
            id="gate_2",
            item_id_getter=operator.itemgetter(1),
            items="gate_2_buttons",
            on_click=gate_2_reply,
        ),
    ),
    parse_mode=ParseMode.HTML,
    state=States.gate_state_2,
    getter=gate_2_inline,
)


gate_window_3 = Window(
    Format("{gate_3_title}"),
    MessageInput(gate_3_reply, ContentType.TEXT),
    parse_mode=ParseMode.HTML,
    state=States.gate_state_3,
    getter=gate_3_inline,
)


main_menu_window = Window(
    StaticMedia(url="https://telegra.ph//file/0a899a91b7084ff6d4e64.jpg"),
    Format("{title}"),
    Row(
        WebApp(Const("Test"), Const("https://github.com/StasKazakov")),
        Select(
            Format("{item[0]}"),
            id="menu",
            item_id_getter=operator.itemgetter(1),
            items="main_menu",
            on_click=main_menu_reply,
        ),
    ),
    parse_mode=ParseMode.HTML,
    state=States.main_menu_state,
    getter=main_menu_inline,
)

menu_sections_window = Window(
    StaticMedia(url="https://telegra.ph//file/0a899a91b7084ff6d4e64.jpg"),
    Format("{title}"),
    Row(
        Select(
            Format("{item[0]}"),
            id="menu_sections_1",
            item_id_getter=operator.itemgetter(1),
            items="menu_sections_1",
            on_click=menu_sections_reply,
        ),
    ),
    Row(
        Select(
            Format("{item[0]}"),
            id="menu_sections_2",
            item_id_getter=operator.itemgetter(1),
            items="menu_sections_2",
            on_click=menu_sections_reply,
        ),
    ),
    Row(
        Select(
            Format("{item[0]}"),
            id="menu_sections_3",
            item_id_getter=operator.itemgetter(1),
            items="menu_sections_3",
            on_click=menu_sections_reply,
        ),
    ),
    Row(
        Select(
            Format("{item[0]}"),
            id="menu_sections_4",
            item_id_getter=operator.itemgetter(1),
            items="menu_sections_4",
            on_click=menu_sections_reply,
        ),
    ),
    SwitchTo(Const("Back"), id="Back", state=States.main_menu_state),
    parse_mode=ParseMode.HTML,
    state=States.menu_sections_state,
    getter=menu_sections_inline,
)


section_photo_window = Window(
    DynamicMedia("section_photo"),
    SwitchTo(Const("Back"), id="Back", state=States.menu_sections_state),
    parse_mode=ParseMode.HTML,
    state=States.section_photo_state,
    getter=section_photo_inline,
)


admin_window = Window(
    Format("{title}"),
    Row(
        Select(
            Format("{item[0]}"),
            id="admin",
            item_id_getter=operator.itemgetter(1),
            items="admin",
            on_click=admin_panel_reply,
        ),
    ),
    SwitchTo(Const("Back"), id="Back", state=States.main_menu_state),
    parse_mode=ParseMode.HTML,
    state=States.admin_panel_state,
    getter=admin_panel_inline,
)


add_item_window = Window(
    Format("{title}"),
    Format("{condition}"),
    MessageInput(add_menu_reply, ContentType.ANIMATION),
    SwitchTo(Const("Back"), id="Back", state=States.admin_panel_state),
    parse_mode=ParseMode.HTML,
    state=States.add_item_state,
    getter=add_menu_inline,
)


#
#
# access_window = Window(
#     Format('{header}'),
#     MessageInput(access_reply, ContentType.TEXT),
#     parse_mode=ParseMode.HTML,
#     state=States.access_state,
#     getter=access_inline
# )
#
#
# main_window = Window(
#     Format("{title}"),
#     Row(
#         SwitchInlineQuery_2(
#             Const("🛒 Market 🛒"),
#             Const(''),
#             ),
#     ),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="menu",
#             item_id_getter=operator.itemgetter(1),
#             items='main_menu',
#             on_click=main_menu_reply
#             ),
#         ),
#     parse_mode=ParseMode.HTML,
#     state=States.main_menu_state,
#     getter=main_window_inline
# )
#
#
# ref_link_window = Window(
#     Format("{title}"),
#     Format("{ref_info}"),
#     SwitchTo(Const("Back"), id="Back", state=States.main_menu_state),
#     parse_mode=ParseMode.HTML,
#     state=States.ref_link_state,
#     getter=ref_link_inline,
# )
#
# feedback_window = Window(
#     Format("{title}"),
#     Format("{contact}"),
#     SwitchTo(Const("Back"), id="Back", state=States.main_menu_state),
#     parse_mode=ParseMode.HTML,
#     state=States.feedback_state,
#     getter=feedback_inline,
# )
#
# admin_window = Window(
#     Format("{title}"),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="admin1",
#             item_id_getter=operator.itemgetter(1),
#             items='admin_1',
#             on_click=admin_panel_reply
#         ),
#     ),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="admin2",
#             item_id_getter=operator.itemgetter(1),
#             items='admin_2',
#             on_click=admin_panel_reply
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=States.main_menu_state),
#     parse_mode=ParseMode.HTML,
#     state=States.admin_panel_state,
#     getter=admin_panel_inline
# )
#
#
#
#
# add_item_window = Window(
#     Format("{title}"),
#     Format("{condition}"),
#     MessageInput(add_item_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=States.admin_panel_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_item_state,
#     getter=add_item_inline
# )
#
#
#
#
# add_description_window = Window(
#     Format("{title}"),
#     Format("{title_item}"),
#     Format("{condition}"),
#     MessageInput(add_description_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=States.add_item_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_description_state,
#     getter=add_description_inline,
# )
#
#
#
# add_price_window = Window(
#     Format("{title}"),
#     Format("{title_item}"),
#     Format("{title_description}"),
#     Format("{condition}"),
#     MessageInput(add_price_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=States.add_description_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_price_state,
#     getter=add_price_inline,
# )
#
# add_quantity_window = Window(
#     Format("{title}"),
#     Format("{title_item}"),
#     Format("{title_description}"),
#     Format("{title_price}"),
#     Format("{condition}"),
#     MessageInput(add_quantity_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=States.add_price_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_quantity_state,
#     getter=add_quantity_inline,
# )
#
# add_photo_window = Window(
#     Format("{title}"),
#     Format("{title_item}"),
#     Format("{title_description}"),
#     Format("{title_price}"),
#     Format("{title_quantity}"),
#     Format("{condition}"),
#     MessageInput(add_photo_reply, ContentType.PHOTO),
#     SwitchTo(Const("Back"), id="Back", state=States.add_quantity_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_photo_state,
#     getter=add_photo_inline,
# )
#
#
# add_item_confirmation_window = Window(
#     Format("{title}"),
#     DynamicMedia("title_photo"),
#     Format("{title_item}"),
#     Format("{title_description}"),
#     Format("{title_price}"),
#     Format("{condition}"),
#     MessageInput(add_photo_reply, ContentType.PHOTO),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="buttons",
#             item_id_getter=operator.itemgetter(1),
#             items='buttons',
#             on_click=add_item_confirmation_reply
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=States.add_photo_state),
#     parse_mode=ParseMode.HTML,
#     state=States.add_item_confirmation_state,
#     getter=add_item_confirmation_inline,
# )
#
# item_added_window = Window(
#     Format("{title}"),
#     DynamicMedia("title_photo"),
#     Format("{title_item}"),
#     Format("{title_description}"),
#     Format("{title_price}"),
#     Format("{condition}"),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="buttons",
#             item_id_getter=operator.itemgetter(1),
#             items='buttons',
#             on_click=item_added_reply
#         ),
#     ),
#
#     parse_mode=ParseMode.HTML,
#     state=States.item_added_state,
#     getter=item_added_inline,
# )
#
#
# delete_window = Window(
#     Format("{title}"),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="delete",
#             item_id_getter=operator.itemgetter(1),
#             items='delete_item',
#             on_click=delete_item_reply
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=States.admin_panel_state),
#     parse_mode=ParseMode.HTML,
#     state=States.delete_item_state,
#     getter=delete_item_inline
# )
#
#
# confirmed_item_delete_window = Window(
#     Format("{title}"),
#     SwitchTo(Const("To Admin Panel"), id="admin_panel", state=States.admin_panel_state),
#     parse_mode=ParseMode.HTML,
#     state=States.confirmed_item_delete_state,
#     getter=confirmed_item_delete_inline
# )

# us_window = Window(
#     Format("{title}"),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="add",
#             item_id_getter=operator.itemgetter(1),
#             items='add_item',
#             on_click=
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=States.admin_panel_state),
#     parse_mode=ParseMode.HTML,
#     state=States.,
#     getter=admin_panel_inline
# )


# DynamicMedia("pic"),
#
#
#
# register_window = Window(
#     parse_mode=ParseMode.HTML,
#     state=States.register_state,
#
# )


# option_action_window = Window(
#     Format("{title}"),
#     Format("{confirm_button}"),
#     Format("{option_action_data}"),
#     MessageInput(new_link_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.link_options_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.option_action_state,
#     getter=option_action_inline
# )


# choose_lang_window = Window(
#     Const('Обрати мову/Chose language/Выберите язык'),
#     Row(
#         Select(
#             Format("{item[0]}"),
#             id="second_window_c",
#             item_id_getter=operator.itemgetter(1),
#             items='lang',
#             on_click=choose_lang_reply
#         ),
#     ),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.choose_lang_state,
#     getter=choose_lang
# )
#
#
#
#
# main_menu_window = Window(
#     Format("{title}"),
#     Column(
#         Select(
#             Format("{item[0]}"),
#             id="main_menu_1",
#             item_id_getter=operator.itemgetter(1),
#             items='title_buttons_1',
#             on_click=main_menu_reply
#         ),
#         Select(
#             Format("{item[0]}"),
#             id="main_menu_2",
#             item_id_getter=operator.itemgetter(1),
#             items="title_buttons_2",
#             on_click=main_menu_reply,
#
#         ),
#     ),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.main_menu_state,
#     getter=main_menu_inline
# )
#
#
# links_list_window = Window(
#     Format("{links_title}"),
#     Column(
#         Select(
#             Format("{item[0]}"),
#             id="option_list",
#             item_id_getter=operator.itemgetter(1),
#             items='links_info',
#             on_click=links_list_reply
#         ),
#     ),
#     MessageInput(new_link_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.main_menu_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.links_list_state,
#     getter=links_list_inline
# )
#
#
# add_link_window = Window(
#     Format("{title}"),
#     Format("{confirm_button}"),
#     MessageInput(new_link_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.links_list_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.add_link_state,
#     getter=add_link_inline
# )
#
#
#
# link_options_window = Window(
#     Format("{title}"),
#     Column(
#         Select(
#             Format("{item[0]}"),
#             id="link_options",
#             item_id_getter=operator.itemgetter(1),
#             items='link_option_buttons',
#             on_click=link_options_reply
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.links_list_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.link_options_state,
#     getter=link_options_inline
# )
#
# option_action_window = Window(
#     Format("{title}"),
#     Format("{confirm_button}"),
#     Format("{option_action_data}"),
#     MessageInput(new_link_reply, ContentType.TEXT),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.link_options_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.option_action_state,
#     getter=option_action_inline
# )
#
#
# del_link_window = Window(
#     Format("{title}"),
#     Column(
#         Select(
#             Format("{item[0]}"),
#             id="del_action",
#             item_id_getter=operator.itemgetter(1),
#             items='confirm_button',
#             on_click=del_action_reply
#         ),
#     ),
#     SwitchTo(Const("Back"), id="Back", state=LinkBot.link_options_state),
#     parse_mode=ParseMode.HTML,
#     state=LinkBot.del_link_state,
#     getter=del_action_inline
# )

from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart
from keyboards.start_menu import menu, menu2, menu3, menu4, menu5
start_router: Router = Router()
@start_router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer(f"Assalomu alaykum {msg.from_user.full_name}  xush kelibsiz!", reply_markup=menu)

@start_router.message(F.text=="Darslarni boshlash")
async def dars_handler(msg: Message):
    await msg.answer("Quyidagi bo'limlardan birini tanlang", reply_markup=menu2)

@start_router.message(F.text=="Dasturlash")
async def dasturlash(msg:Message):
    await msg.answer("Kursni tanlang: ", reply_markup=menu3)

@start_router.message(F.text=="Front-end")
async def front(msg:Message):
    await msg.answer("Kursni tanlang: ", reply_markup=menu4)

@start_router.message(F.text=="HTML")
async def html(msg:Message):
    await msg.answer("Dars sonini tanlang", reply_markup=menu5)

@start_router.message(F.text=="0-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANUZpym9GAMeiUQYXDvUu_t4CamuK0AAhYLAAJbWZlIjUdTG5XAaw41BA", caption="HTML Darslari | 0-dars | Kurs haqida")

@start_router.message(F.text=="1-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANYZpyoo0UBvEKbxl_C_GjA2HS67bwAAhcLAAJbWZlIkDRz7C7fOG81BA", caption="HTML Darslari | 1-dars | WEB haqida ")

@start_router.message(F.text=="2-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANaZpyo43d7NznbWDpvP5DDnidLhB0AAsoMAAJQv4FL08WY_fp3H7w1BA", caption="HTML Darslari | 2-dars | Kirish ")

@start_router.message(F.text=="3-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANcZpypGPEVkeZafLyzx_9qqNgNEoMAAhoLAAJbWZlIxLDeoU49Tcg1BA", caption="HTML Darslari | 3-dars | Development Environment (Dasturlash Muhiti) ")

@start_router.message(F.text=="4-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANeZpypSRXMakpwSAk-0thF0YChhvQAAhwLAAJbWZlIcTDrfsP03nQ1BA", caption="HTML Darslari | 4-dars | Hujjat strukturasi va '!DOCTYPE' ")

@start_router.message(F.text=="5-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANgZpyphRWq2tHkdTfQkK_VKkTpbDIAAh0LAAJbWZlIwLD6DnzO9rw1BA", caption="HTML Darslari | 5-dars | Elementlar va 'attribute'lar ")

@start_router.message(F.text=="6-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANiZpypsI9bn8fj1zfQmgQWdJi50ksAAppJAALFeClJd9I62gPJ6mE1BA", caption="HTML Darslari | 6-dars | 'Headings' (Sarlavhalar) ")

@start_router.message(F.text=="7-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANkZpyp6QFuEDdnKQ_Jol2FU-kX6-sAAmEMAALYJaBLNZZCkXxL8nU1BA", caption="HTML Darslari | 7-dars | 'Paragraphs' (Xatboshilar) ")

@start_router.message(F.text=="8-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANmZpyqEZzW2UtzeX6l4HxfljPjTqsAAh8LAAJbWZlION-LxogK89c1BA", caption="HTML Darslari | 8-dars | Styles (Stillar) ")

@start_router.message(F.text=="9-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANoZpyqOZIOhdpAlFQGr4oJwjiY-OUAAmIMAALYJaBLAAH8GxRAC4qZNQQ", caption="HTML Darslari | 9-dars | Formatting (Formatlash) ")

@start_router.message(F.text=="10-dars")
async def dars0(msg:Message):
    await msg.answer_video("BAACAgIAAxkBAANqZpyqYO9yN0z4PM6_-f_eV3iUqAMAAiALAAJbWZlI2aD-axnLzaA1BA", caption="HTML Darslari | 10-dars | Comments (Izohlar) ")




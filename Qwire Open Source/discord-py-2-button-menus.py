import discord # requires v2.0.0a

class PagesView(discord.ui.View):
    def __init__(self, *args, **kwargs):
        self.msg = None
        self.user = kwargs.pop('user', discord.Object(id=0))
        self.indexes = kwargs.pop('indexes', False)
        self.pages = kwargs.pop('pages')
        self.delete_after = kwargs.pop('delete_after', False)
        self.current = 0
        super().__init__(*args, **kwargs)
    @discord.ui.button(label="", emoji="⏮️", disabled=True)
    async def fast_previous(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        current = 0
        self.children[0].disabled = True
        self.children[1].disabled = True
        self.children[3].disabled = False
        self.children[4].disabled = False
        if isinstance(self.pages[self.current], discord.Embed):
            temp = self.pages[self.current]
            if self.indexes:
                temp.set_footer(text=f"{self.current+1}/{len(self.pages)}")
            await interaction.response.edit_message(content=None, embed=temp, view=self)
        #elif isinstance(self.pages[self.current], discord.File):
        #    await interaction.response.edit_message(content=None, embed=None, file=self.pages[self.current], view=self)
        elif isinstance(self.pages[self.current], str):
            temp = self.pages[self.current]
            if self.indexes:
                temp = temp+f"\n\n{self.current+1}/{len(self.pages)}"
            await interaction.response.edit_message(content=self.pages[self.current], embed=None, view=self)
    @discord.ui.button(label="", emoji="⬅️", disabled=True)
    async def previous(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.current -= 1
        if self.current == 0:
            self.children[0].disabled = True
            self.children[1].disabled = True
        self.children[3].disabled = False
        self.children[4].disabled = False
        if isinstance(self.pages[self.current], discord.Embed):
            temp = self.pages[self.current]
            if self.indexes:
                temp.set_footer(text=f"{self.current+1}/{len(self.pages)}")
            await interaction.response.edit_message(content=None, embed=temp, view=self)
        #elif isinstance(self.pages[self.current], discord.File):
        #    await interaction.response.edit_message(content=None, embed=None, file=self.pages[self.current], view=self)
        elif isinstance(self.pages[self.current], str):
            temp = self.pages[self.current]
            if self.indexes:
                temp = temp+f"\n\n{self.current+1}/{len(self.pages)}"
            await interaction.response.edit_message(content=self.pages[self.current], embed=None, view=self)
    @discord.ui.button(label="", emoji="⏹️")
    async def finish(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        if self.delete_after == False:
            for i in self.children:
                i.disabled = True
            await interaction.response.edit_message(view=self)
        else:
            await self.msg.delete()
        self.stop()
    @discord.ui.button(label="", emoji="➡️")
    async def next(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.current += 1
        if self.current == len(self.pages)-1:
            self.children[3].disabled = True
            self.children[4].disabled = True
        self.children[0].disabled = False
        self.children[1].disabled = False
        if isinstance(self.pages[self.current], discord.Embed):
            temp = self.pages[self.current]
            if self.indexes:
                temp.set_footer(text=f"{self.current+1}/{len(self.pages)}")
            await interaction.response.edit_message(content=None, embed=temp, view=self)
        #elif isinstance(self.pages[self.current], discord.File):
        #    await interaction.response.edit_message(content=None, embed=None, file=self.pages[self.current], view=self)
        elif isinstance(self.pages[self.current], str):
            temp = self.pages[self.current]
            if self.indexes:
                temp = temp+f"\n\n{self.current+1}/{len(self.pages)}"
            await interaction.response.edit_message(content=self.pages[self.current], embed=None, view=self)
    @discord.ui.button(label="", emoji="⏭️")
    async def fast_next(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        current = len(self.pages)-1
        self.children[0].disabled = False
        self.children[1].disabled = False
        self.children[3].disabled = True
        self.children[4].disabled = True
        if isinstance(self.pages[self.current], discord.Embed):
            temp = self.pages[self.current]
            if self.indexes:
                temp.set_footer(text=f"{self.current+1}/{len(self.pages)}")
            await interaction.response.edit_message(content=None, embed=temp, view=self)
        #elif isinstance(self.pages[self.current], discord.File):
        #    await interaction.response.edit_message(content=None, embed=None, file=self.pages[self.current], view=self)
        elif isinstance(self.pages[self.current], str):
            temp = self.pages[self.current]
            if self.indexes:
                temp = temp+f"\n\n{self.current+1}/{len(self.pages)}"
            await interaction.response.edit_message(content=self.pages[self.current], embed=None, view=self)
    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

class Confirm(discord.ui.View):
    def __init__(self, *args, **kwargs):
        self.msg = None
        self.user = kwargs.pop('user', discord.Object(id=0))
        self.answer = None
        super().__init__(*args, **kwargs)
    @discord.ui.button(label="", emoji="✅", style=discord.ButtonStyle.primary)
    async def yes_please(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.answer = True
        for i in self.children:
            i.disabled = True
        await interaction.response.edit_message(view=self)
        self.stop()
    @discord.ui.button(label="", emoji="❌", style=discord.ButtonStyle.primary)
    async def no_thanks(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.answer = False
        for i in self.children:
            i.disabled = True
        await interaction.response.edit_message(view=self)
        self.stop()
    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

class Cleanup(discord.ui.View):
    def __init__(self, *args, **kwargs):
        self.msg = None
        self.user = kwargs.pop('user', discord.Object(id=0))
        super().__init__(*args, **kwargs)
    @discord.ui.button(label="", emoji="⏹️")
    async def get_out_now(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        await self.msg.delete()
        self.stop()
    
    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

class Choice(discord.ui.View):
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices')
        self.user = kwargs.pop('user', discord.Object(id=0))
        self.current = 0
        self.delete_after = kwargs.pop('delete_after', False)
        self.option = None
        self.msg = None
        super().__init__(*args, **kwargs)
    @discord.ui.button(label="Previous", emoji="⏪", disabled=True)
    async def previous(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.current -= 1
        if self.current == 0:
            self.children[0].disabled = True
        self.children[3].disabled = False
        if isinstance(self.choices[self.current], discord.Embed):
            await interaction.response.edit_message(content=None, embed=self.choices[self.current], view=self)
        elif isinstance(self.choices[self.current], discord.File):
            await interaction.response.edit_message(content=None, embed=None, file=self.choices[self.current], view=self)
        elif isinstance(self.choices[self.current], str):
            await interaction.response.edit_message(content=self.choices[self.current], embed=None, view=self)

    @discord.ui.button(label="Yes, this one", emoji="✅", style=discord.ButtonStyle.primary)
    async def this_one(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        for i in self.children:
            i.disabled = True
        await interaction.response.edit_message(view=self)
        self.option = self.choices[self.current]
        self.stop()
    @discord.ui.button(label="Cancel", emoji="❌", style=discord.ButtonStyle.primary)
    async def cancel(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        for i in self.children:
            i.disabled = True
        await interaction.response.edit_message(view=self)
        self.stop()
    @discord.ui.button(label="Next", emoji="⏩")
    async def next(self, button, interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.pong()
        self.current += 1
        if self.current == len(self.choices)-1:
            self.children[3].disabled = True
        self.children[0].disabled = False
        if isinstance(self.choices[self.current], discord.Embed):
            await interaction.response.edit_message(content=None, embed=self.choices[self.current], view=self)
        elif isinstance(self.choices[self.current], discord.File):
            await interaction.response.edit_message(content=None, embed=None, file=self.choices[self.current], view=self)
        elif isinstance(self.choices[self.current], str):
            await interaction.response.edit_message(content=self.choices[self.current], embed=None, view=self)
    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        self.option = False
        await self.msg.edit(view=self)



class CustomContext(discord.ext.commands.Context):
    async def choice(self, choices, user=None, timeout=120, delete_after=False):
        if user == None:
            user = self.author
        view = Choice(choices=choices, timeout=120, delete_after=delete_after)
        if isinstance(choices[0], discord.Embed):
            view.msg = await self.send(embed=choices[0], view=view)
        elif isinstance(choices[0], str):
            view.msg = await self.send(choices[0], view=view)
        res = await view.wait()
        return [view.option, view.msg]
    async def cleanup(self, what, user=None, timeout=120):
        if user == None:
            user = self.author
        view = Cleanup(timeout=timeout)
        if isinstance(what, discord.Embed):
            view.msg = await self.send(embed=what, view=view)
        elif isinstance(what, str):
            view.msg = await self.send(what, view=view)

    async def confirm(self, what, user=None, timeout=120):
        if user == None:
            user = self.author
        view = Confirm(timeout=timeout)
        if isinstance(what, discord.Embed):
            view.msg = await self.send(embed=what, view=view)
        elif isinstance(what, str):
            view.msg = await self.send(what, view=view)
        res = await view.wait()
        if res == True:
            return [None, view.msg]
        return [view.answer, view.msg]

    async def paginate(self, pages, user=None, timeout=120, indexes=False, delete_after=False):
        if user == None:
            user = self.author
        view = PagesView(pages=pages, timeout=timeout, indexes=indexes, delete_after=delete_after)
        if isinstance(pages[0], discord.Embed):
            temp = pages[0]
            if indexes == True:
                temp.set_footer(f'1/{len(pages)}')
            view.msg = await self.send(embed=temp, view=view)
        elif isinstance(pages[0], str):
            temp = pages[0]
            if indexes == True:
                temp = temp+f'\n\n1/{len(pages)}'
            view.msg = await self.send(pages[0], view=view)

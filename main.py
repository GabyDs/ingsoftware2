import sqlite3
import flet as ft

PADDING = 30
TEXT_SIZE = 24

def main(page: ft.Page):
    page.title = "NavigationBar Example"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CALENDAR_TODAY),
        title=ft.Text("Today"),
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.PERSON_OUTLINE,
                selected_icon=ft.icons.PERSON,
                label="Profile"),
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_OUTLINED,
                selected_icon=ft.icons.CALENDAR_MONTH,
                label="Diary"),
            ft.NavigationDestination(
                icon=ft.icons.ANALYTICS_OUTLINED,
                selected_icon=ft.icons.ANALYTICS,
                label="Stats"),
        ]
    )

    breakfast = ft.Card(content=ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.WB_TWILIGHT),
            ft.Text("Breakfast", size=TEXT_SIZE),
            ft.FloatingActionButton(icon=ft.icons.ADD)
        ]),
        padding=PADDING,
    ))
    lunch = ft.Card(content=ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.WB_SUNNY),
            ft.Text("Lunch", size=TEXT_SIZE),
            ft.FloatingActionButton(icon=ft.icons.ADD)
        ]),
        padding=PADDING,
    ))
    dinner = ft.Card(content=ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.BEDTIME),
            ft.Text("Dinner", size=TEXT_SIZE),
            ft.FloatingActionButton(icon=ft.icons.ADD)
        ]),
        padding=PADDING,
    ))
    snacks = ft.Card(content=ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.RESTAURANT),
            ft.Text("Snacks", size=TEXT_SIZE),
            ft.FloatingActionButton(icon=ft.icons.ADD)
        ]),
        padding=PADDING,
    ))

    page.add(
    ft.Column(controls=[
        breakfast,
        lunch,
        dinner,
        snacks,
    ],
    ))


ft.app(target=main)
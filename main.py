import sqlite3
import flet as ft

def main(page: ft.Page):
    page.title = "NavigationBar Example"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALLET),
        title=ft.Text("AppBar Example"),
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
    page.add(ft.Text("Body!"))

ft.app(target=main)
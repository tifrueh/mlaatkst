project(
    'MLAatKST',
    'cpp',
    default_options: [ 'cpp_std=c++17' ],
    license: 'GPL-3.0-or-later',
    license_files: 'LICENSE',
    version: '2.0.0'
)

run_command(
    'xgettext',
    '-o' + meson.current_source_dir() + '/resources/lang/de/LC_MESSAGES/messages.po',
    '--copyright-holder="Timo Früh"',
    '--package-name="MLAatKST"',
    '--msgid-bugs-address="timo.frueh@icloud.com"',
    '--join-existing',
    meson.current_source_dir() + '/src/main.cpp',
    meson.current_source_dir() + '/src/mainframe.cpp',
    meson.current_source_dir() + '/src/quotation_formatter.cpp',
    meson.current_source_dir() + '/src/toppanel.cpp',
    check: true
)

incdir = include_directories('include')

srcs = [
    'src/id.cpp',
    'src/main.cpp',
    'src/mainframe.cpp',
    'src/quotation_formatter.cpp',
    'src/toppanel.cpp'
]

wx = dependency('wxwidgets')

deps = [ wx ]

executable(
    'MLAatKST',
    srcs,
    dependencies: deps,
    include_directories: incdir,
    win_subsystem: 'windows'
)

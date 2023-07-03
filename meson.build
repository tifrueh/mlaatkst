project(
    'mlaatkst',
    'cpp',
    default_options: [ 'cpp_std=c++17' ],
    license: 'GPL-3.0-or-later',
    license_files: 'LICENSE',
    version: '2.1.2'
)

incdir = include_directories([ 'include', 'img' ])

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
    win_subsystem: 'windows',
    install: true
)

install_data(
    'resources/lang/de/LC_MESSAGES/mlaatkst.mo',
    install_dir: get_option('localedir') / 'de' / 'LC_MESSAGES'
)

install_data(
    'resources/mlaatkst.png'
)

install_data(
    'resources/mlaatkst.desktop'
)

project(
    'MLAatKST',
    'cpp',
    default_options: [ 'cpp_std=c++17' ],
    license: 'GPL-3.0-or-later',
    license_files: 'LICENSE',
    version: '2.0.0'
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

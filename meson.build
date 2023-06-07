project(
    'MLAatKST',
    'cpp',
    default_options: [ 'cpp_std=c++17' ],
    license: 'GPL-3.0-or-later',
    license_files: 'LICENSE',
    version: '2.0.0-dev'
)

srcs = [
    'src/main.cpp'
]

wx = dependency('wxwidgets')

deps = [ wx ]

executable(
    'MLAatKST',
    srcs,
    dependencies: deps,
    win_subsystem: 'windows'
)

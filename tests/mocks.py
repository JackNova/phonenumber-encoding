sample_dictionary = """an
                    blau
                    Bo"
                    Boot
                    bo"s
                    da
                    Fee
                    fern
                    Fest
                    fort
                    je
                    jemand
                    mir
                    Mix
                    Mixer
                    Name
                    neu
                    o"d
                    Ort
                    so
                    Tor
                    Torf
                    Wasser""".splitlines()

sample_phones = """112
                5624-82
                4824
                0721/608-4067
                10/783--5
                1078-913-5
                381482
                04824""".splitlines()

correct_output = """5624-82: mir Tor
                5624-82: Mix Tor
                4824: Torf
                4824: fort
                4824: Tor 4
                10/783--5: neu o"d 5
                10/783--5: je bo"s 5
                10/783--5: je Bo" da
                381482: so 1 Tor
                04824: 0 Torf
                04824: 0 fort
                04824: 0 Tor 4""".splitlines()
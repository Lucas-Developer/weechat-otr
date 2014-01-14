# pylint: disable=missing-docstring
# pylint: disable=no-method-argument
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods
# pylint: disable=unused-argument

from __future__ import unicode_literals

import copy
import types

class MockWeechat(types.ModuleType):

    WEECHAT_RC_ERROR = None
    WEECHAT_RC_OK = None

    def __init__(self):
        self.config_options = {}
        self.script_name = None
        self.printed = {}

    def save(self):
        self.saved_state = copy.deepcopy(self.__dict__)

    def restore(self):
        prev_state = copy.deepcopy(self.saved_state)
        self.__dict__.clear()
        self.__dict__.update(prev_state)

    def bar_item_new(*args):
        pass

    def bar_item_update(*args):
        pass

    def buffer_get_string(self, buf, string):
        buffers = {
            None : {
                b'localvar_type' : b'private',
                b'localvar_channel' : b'nick',
                b'localvar_server' : b'server',
                },
            b'server_nick_buffer' : {
                b'localvar_type' : b'private',
                b'localvar_channel' : b'nick',
                b'localvar_server' : b'server',
                },
            b'server_nick2_buffer': {
                b'localvar_type' : b'private',
                b'localvar_channel' : b'nick2',
                b'localvar_server' : b'server',
                },
            b'non_private_buffer' : {
                b'localvar_type' : b'non_private',
                }
            }

        return buffers[buf].get(string)

    def command(*args):
        pass

    def config_boolean(self, s):
        if s == 'on':
            return 1
        else:
            return 0

    def config_get(self, key):
        return self.config_options.get(key, '')

    def config_new(*args):
        pass

    def config_new_option(self, config_file, section, name, *args):
        parts = [self.script_name]
        if section is not None:
            parts.append(section)
        parts.append(name)
        default = args[5]
        full_option_name = '.'.join(parts)

        self.config_options[full_option_name] = default

    def config_new_section(self, config_file, name, *args):
        return name

    def config_read(*args):
        pass

    def current_buffer(*args):
        pass

    def hook_command(*args):
        pass

    def hook_completion(*args):
        pass

    def hook_config(*args):
        pass

    def hook_modifier(*args):
        pass

    def hook_signal(*args):
        pass

    def info_get(self, name, *args):
        infos = {
            (b'',) : {
                b'weechat_dir': b'/tmp/weechat',
                },
            (b'server',) : {
                b'irc_nick': b'nick',
                },
            (b'server,nick',) : {
                b'irc_buffer' : b'server_nick_buffer',
                },
            (b'server,no_window_nick',) : {
                b'irc_buffer' : b'non_private_buffer',
                },
        }

        return infos[args].get(name)

    def infolist_free(*args):
        pass

    def infolist_get(*args):
        pass

    def infolist_next(*args):
        pass

    def mkdir_home(self, *args):
        pass

    def prnt(self, buf, message):
        self.printed.setdefault(buf, []).append(message)

    def register(self, script_name, *args):
        self.script_name = script_name

        return True


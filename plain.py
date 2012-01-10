# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - modern theme

    @copyright: 2003-2005 Nir Soffer, Thomas Waldmann
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin.theme import ThemeBase

class Theme(ThemeBase):

    name = "plain"

    _ = lambda x: x     # We don't have gettext at this moment, so we fake it
    icons = {
        # key         alt                        icon filename      w   h
        # FileAttach
        'attach':     ("%(attach_count)s",       "moin-attach.png", 16, 16),
        'info':     ("[INFO]",       "moin-info.png", 16, 16),
        'attachimg':  (_("[ATTACH]"),            "attach.png",      32, 32),
        # RecentChanges
        'rss':        (_("[RSS]"),               "moin-rss.png",    16, 16),
        'deleted':    (_("[DELETED]"),           "moin-deleted.png",16, 16),
        'updated':    (_("[UPDATED]"),           "moin-updated.png",16, 16),
        'renamed':    (_("[RENAMED]"),           "moin-renamed.png",16, 16),
        'conflict':   (_("[CONFLICT]"),          "moin-conflict.png", 16, 16),
        'new':        (_("[NEW]"),               "moin-new.png",    16, 16),
        'diffrc':     (_("[DIFF]"),              "moin-diff.png",   16, 16),
        # General
        'bottom':     (_("[BOTTOM]"),            "moin-bottom.png", 16, 16),
        'top':        (_("[TOP]"),               "moin-top.png",    16, 16),
        'www':        ("[WWW]",                  "moin-www.png",    16, 16),
        'mailto':     ("[MAILTO]",               "moin-email.png",  16, 16),
        'news':       ("[NEWS]",                 "moin-news.png",   16, 16),
        'telnet':     ("[TELNET]",               "moin-telnet.png", 16, 16),
        'ftp':        ("[FTP]",                  "moin-ftp.png",    16, 16),
        'file':       ("[FILE]",                 "moin-ftp.png",    16, 16),
        # search forms
        'searchbutton': ("[?]",                  "moin-search.png", 16, 16),
        'interwiki':  ("[%(wikitag)s]",          "moin-inter.png",  16, 16),

        # smileys (this is CONTENT, but good looking smileys depend on looking
        # adapted to the theme background color and theme style in general)
        #vvv    ==      vvv  this must be the same for GUI editor converter
        'X-(':        ("X-(",                    'angry.png',       16, 16),
        ':D':         (":D",                     'biggrin.png',     16, 16),
        '<:(':        ("<:(",                    'frown.png',       16, 16),
        ':o':         (":o",                     'redface.png',     16, 16),
        ':(':         (":(",                     'sad.png',         16, 16),
        ':)':         (":)",                     'smile.png',       16, 16),
        'B)':         ("B)",                     'smile2.png',      16, 16),
        ':))':        (":))",                    'smile3.png',      16, 16),
        ';)':         (";)",                     'smile4.png',      16, 16),
        '/!\\':       ("/!\\",                   'alert.png',       16, 16),
        '<!>':        ("<!>",                    'attention.png',   16, 16),
        '(!)':        ("(!)",                    'idea.png',        16, 16),
        ':-?':        (":-?",                    'tongue.png',      16, 16),
        ':\\':        (":\\",                    'ohwell.png',      16, 16),
        '>:>':        (">:>",                    'devil.png',       16, 16),
        '|)':         ("|)",                     'tired.png',       16, 16),
        ':-(':        (":-(",                    'sad.png',         16, 16),
        ':-)':        (":-)",                    'smile.png',       16, 16),
        'B-)':        ("B-)",                    'smile2.png',      16, 16),
        ':-))':       (":-))",                   'smile3.png',      16, 16),
        ';-)':        (";-)",                    'smile4.png',      16, 16),
        '|-)':        ("|-)",                    'tired.png',       16, 16),
        '(./)':       ("(./)",                   'checkmark.png',   16, 16),
        '{OK}':       ("{OK}",                   'thumbs-up.png',   16, 16),
        '{X}':        ("{X}",                    'icon-error.png',  16, 16),
        '{i}':        ("{i}",                    'icon-info.png',   16, 16),
        '{1}':        ("{1}",                    'prio1.png',       15, 13),
        '{2}':        ("{2}",                    'prio2.png',       15, 13),
        '{3}':        ("{3}",                    'prio3.png',       15, 13),
        '{*}':        ("{*}",                    'star_on.png',     16, 16),
        '{o}':        ("{o}",                    'star_off.png',    16, 16),
    }
    del _

    def header(self, d, **kw):
        """ Assemble wiki header

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """
        html = [
            # Pre header custom html
            self.emit_custom_html(self.cfg.page_header1),

            # Header
            u'<div id="header">',
            self.logo(),
            self.searchform(d),
            u'<div id="locationline">',
            self.interwiki(d),
            self.title(d),
            u'</div>',
            self.trail(d),
            u'<div id="pageline"><hr style="display:none;"></div>',
            self.navibar(d),
            u'</div>',
            self.msg(d),

            # Post header custom html (not recommended)
            self.emit_custom_html(self.cfg.page_header2),

            # Start of page
            self.startPage(),
        ]
        return u'\n'.join(html)

    def editorheader(self, d, **kw):
        """ Assemble wiki header for editor

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """
        html = [
            # Pre header custom html
            self.emit_custom_html(self.cfg.page_header1),

            # Header
            u'<div id="header">',
            self.title(d),
            self.msg(d),
            u'</div>',

            # Post header custom html (not recommended)
            self.emit_custom_html(self.cfg.page_header2),

            # Start of page
            self.startPage(),
        ]
        return u'\n'.join(html)

    def footer(self, d, **keywords):
        """ Assemble wiki footer

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """
        page = d['page']
        html = [
            # End of page
            self.pageinfo(page),
            self.endPage(),

            # Pre footer custom html (not recommended!)
            self.emit_custom_html(self.cfg.page_footer1),

            # Footer
            u'<div id="footer">',
            self.editbar(d),
            self.username(d),
            #self.credits(d),
            #self.showversion(d, **keywords),
            u'</div>',

            # Post footer custom html
            self.emit_custom_html(self.cfg.page_footer2),
            ]
        return u'\n'.join(html)


def execute(request):
    """
    Generate and return a theme object

    @param request: the request object
    @rtype: MoinTheme
    @return: Theme object
    """
    return Theme(request)


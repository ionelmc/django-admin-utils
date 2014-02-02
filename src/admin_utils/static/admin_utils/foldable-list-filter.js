/*  Django Foldable List.
 *
 * https://bitbucket.org/Stanislas/django-foldable-list-filter
 *
 * Copyright 2012, Stanislas Guerra <stanislas.guerra@gmail.com>
 * Licensed under the BSD 2-Clause licence.
 * http://www.opensource.org/licenses/bsd-license.php
 *
 * */

(function($) {
    /*!
     * jQuery Cookie Plugin v1.4.0
     * https://github.com/carhartl/jquery-cookie
     *
     * Copyright 2013 Klaus Hartl
     * Released under the MIT license
     */
    var pluses = /\+/g;

    function encode(s) {
        return config.raw ? s : encodeURIComponent(s);
    }

    function decode(s) {
        return config.raw ? s : decodeURIComponent(s);
    }

    function stringifyCookieValue(value) {
        return encode(config.json ? JSON.stringify(value) : String(value));
    }

    function parseCookieValue(s) {
        if (s.indexOf('"') === 0) {
            // This is a quoted cookie as according to RFC2068, unescape...
            s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
        }

        try {
            // Replace server-side written pluses with spaces.
            // If we can't decode the cookie, ignore it, it's unusable.
            s = decodeURIComponent(s.replace(pluses, ' '));
        } catch (e) {
            return;
        }

        try {
            // If we can't parse the cookie, ignore it, it's unusable.
            return config.json ? JSON.parse(s) : s;
        } catch (e) {}
    }

    function read(s, converter) {
        var value = config.raw ? s : parseCookieValue(s);
        return $.isFunction(converter) ? converter(value) : value;
    }

    var config = $.cookie = function(key, value, options) {

        // Write
        if (value !== undefined && !$.isFunction(value)) {
            options = $.extend({}, config.defaults, options);

            if (typeof options.expires === 'number') {
                var days = options.expires,
                    t = options.expires = new Date();
                t.setDate(t.getDate() + days);
            }

            return (document.cookie = [
                encode(key), '=', stringifyCookieValue(value),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path ? '; path=' + options.path : '',
                options.domain ? '; domain=' + options.domain : '',
                options.secure ? '; secure' : ''
            ].join(''));
        }

        // Read

        var result = key ? undefined : {};

        // To prevent the for loop in the first place assign an empty array
        // in case there are no cookies at all. Also prevents odd result when
        // calling $.cookie().
        var cookies = document.cookie ? document.cookie.split('; ') : [];

        for (var i = 0, l = cookies.length; i < l; i++) {
            var parts = cookies[i].split('=');
            var name = decode(parts.shift());
            var cookie = parts.join('=');

            if (key && key === name) {
                // If second argument (value) is a function it's a converter...
                result = read(cookie, value);
                break;
            }

            // Prevent storing a cookie that we couldn't decode.
            if (!key && (cookie = read(cookie)) !== undefined) {
                result[name] = cookie;
            }
        }

        return result;
    };

    config.defaults = {};

    $.removeCookie = function(key, options) {
        if ($.cookie(key) !== undefined) {
            // Must not alter options, thus extending a fresh object...
            $.cookie(key, '', $.extend({}, options, {
                expires: -1
            }));
            return true;
        }
        return false;
    };

    $(document).ready(function() {
        var flf = {
            filters: $("#changelist-filter h3"),
            cookie_name: "list_filter_closed",
            delim: "|",
            opened_class: "opened",
            closed_class: "closed",
            list_filter_closed: [],
            update_cookie: function(action, index) {
                if ($.isFunction($.cookie)) {
                    var list_filter_closed = flf.get_list_filter_closed();
                    if (action === flf.closed_class) {
                        list_filter_closed.push(index.toString());
                    } else {
                        list_filter_closed.splice(list_filter_closed.indexOf(index.toString()), 1);
                    }
                    $.cookie(flf.cookie_name,
                        list_filter_closed.join(flf.delim));
                }
            },
            get_list_filter_closed: function() {
                return ($.cookie(flf.cookie_name) || "")
                    .split(flf.delim)
            }
        };

        if ($.isFunction($.cookie)) {
            flf.list_filter_closed = flf.get_list_filter_closed();
        }

        flf.filters.each(function(i, elt) {
            var h3 = $(this),
                status_class = flf.opened_class;
            if (flf.list_filter_closed.indexOf(i.toString()) !== -1) {
                status_class = flf.closed_class;
            }
            h3.addClass("filter " + status_class);
        });

        flf.filters.click(function() {
            var filter = $(this);
            if (filter.hasClass(flf.opened_class)) { // Closing.
                filter.removeClass(flf.opened_class);
                filter.addClass(flf.closed_class);
                flf.update_cookie(flf.closed_class, flf.filters.index(filter));
            } else { // Opening.
                filter.addClass(flf.opened_class);
                filter.removeClass(flf.closed_class);
                flf.update_cookie(flf.opened_class, flf.filters.index(filter));
            }
        });
    });

})(django.jQuery);

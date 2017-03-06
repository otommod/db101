from tkinter import ttk

from ..observable import eventsource


class EventedScrollbar(ttk.Scrollbar):
    """A ttk.Scrollbar that emits an event when it is scrolled."""

    @eventsource
    def scrolled(from_, to):
        pass

    def set(self, first, last):
        curfirst, curlast = self.get()
        super(EventedScrollbar, self).set(first, last)
        if curfirst != first or curlast != last:
            self.scrolled((curfirst, curlast), (first, last))

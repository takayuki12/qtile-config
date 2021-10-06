from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus
from libqtile.utils import send_notification
from enum import Enum, unique
from typing import NamedTuple


icons = {
    "battery-10": "",
    "battery-20": "",
    "battery-30": "",
    "battery-40": "",
    "battery-50": "",
    "battery-60": "",
    "battery-70": "",
    "battery-80": "",
    "battery-90": "",
    "battery-10-charge": "",
    "battery-20-charge": "",
    "battery-30-charge": "",
    "battery-40-charge": "",
    "battery-50-charge": "",
    "battery-60-charge": "",
    "battery-70-charge": "",
    "battery-80-charge": "",
    "battery-90-charge": "",
    "battery-full": "",
    "battery-full-charged": "",
    "battery-full-charge": "",
    "battery-missing": "",
    "battery-empty": "",
}

pers = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9
]


class CustomBattery(widget.Battery):
    def __init__(self, **config) -> None:
        super().__init__(**config)

    def poll(self) -> str:
        """Determine the text to display

        Function returning a string with battery information to display on the
        status bar. Should only use the public interface in _Battery to get
        necessary information for constructing the string.
        """
        try:
            status = self._battery.update_status()
        except RuntimeError as e:
            return 'Error: {}'.format(e)

        if self.notify_below:
            percent = int(status.percent * 100)
            if percent < self.notify_below:
                if not self._has_notified:
                    send_notification(
                        "Warning", "Battery at {0}%".format(percent), urgent=True)
                    self._has_notified = True
            elif self._has_notified:
                self._has_notified = False
        return self.build_string(status)

    def build_string(self, status: BatteryStatus) -> str:
        """Determine the string to return for the given battery state

        Parameters
        ----------
        status:
            The current status of the battery

        Returns
        -------
        str
            The string to display for the current status.
        """
        char = ''

        if self.hide_threshold is not None and status.percent > self.hide_threshold:
            return ''

        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground

        if status.state == BatteryState.CHARGING:
            for p in pers:
                if status.percent <= p:
                    pr = int(p*100)
                    char = icons[f'battery-{pr}-charge']
                    break

            # char = self.charge_char
        elif status.state == BatteryState.DISCHARGING:
            for p in pers:
                if status.percent <= p:
                    pr = int(p*100)
                    char = icons[f'battery-{pr}']
                    break
            # char = self.discharge_char
        elif status.state == BatteryState.FULL:
            if self.show_short_text:
                return "Full"
            char = icons["battery-full"]
            # char = self.full_charO
        elif status.state == BatteryState.EMPTY or \
                (status.state == BatteryState.UNKNOWN and status.percent == 0):
            if self.show_short_text:
                return "Empty"
            char = self.empty_char
        else:
            char = self.unknown_char

        hour = status.time // 3600
        minute = (status.time // 60) % 60

        # char = icons["battery-40"]

        return self.format.format(
            char=char,
            percent=status.percent,
            watt=status.power,
            hour=hour,
            min=minute
        )

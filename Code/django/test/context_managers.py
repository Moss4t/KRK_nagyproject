import contextlib

import mock


# Originaly comes from mock-django (https://github.com/dcramer/mock-django)
@contextlib.contextmanager
def mock_signal_receiver(signal, wraps=None, **kwargs):
    if wraps is None:
        wraps = lambda *args, **kwargs: None

    receiver = mock.Mock(wraps=wraps)
    signal.connect(receiver, **kwargs)
    yield receiver
    signal.disconnect(receiver)

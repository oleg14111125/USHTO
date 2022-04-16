from duty.objects import dp, MySignalEvent, __version__
from duty.utils import ment_user, format_response
from .updating import get_last_version


@dp.longpoll_event_register('инфо', 'инфа', '-i', 'info')
@dp.my_signal_event_register('инфо', 'инфа', '-i', 'info')
def info(event: MySignalEvent) -> str:
    update_info = ''
    )
    event.msg_op(2, update_info + message)
    return "ok"

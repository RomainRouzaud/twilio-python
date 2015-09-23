# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class TranscriptionList(ListResource):

    def __init__(self, domain, account_sid, recording_sid):
        super(TranscriptionList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'recording_sid': recording_sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions.json".format(**self._instance_kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.read(
            self,
            TranscriptionInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            TranscriptionInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class TranscriptionContext(InstanceContext):

    def __init__(self, domain, account_sid, recording_sid, sid):
        super(TranscriptionContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'recording_sid': recording_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json".format(**self._instance_kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            TranscriptionInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class TranscriptionInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, recording_sid, sid=None):
        super(TranscriptionInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._api_version = payload['api_version']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._duration = payload['duration']
        self._owner_account_sid = payload['owner_account_sid']
        self._price = payload['price']
        self._price_unit = payload['price_unit']
        self._recording_sid = payload['recording_sid']
        self._sid = payload['sid']
        self._status = payload['status']
        self._transcription_text = payload['transcription_text']
        self._type = payload['type']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_recording_sid = recording_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TranscriptionContext(
                self._domain,
                self._context_account_sid,
                self._context_recording_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def api_version(self):
        """ The api_version """
        return self._api_version

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def duration(self):
        """ The duration """
        return self._duration

    @property
    def owner_account_sid(self):
        """ The owner_account_sid """
        return self._owner_account_sid

    @property
    def price(self):
        """ The price """
        return self._price

    @property
    def price_unit(self):
        """ The price_unit """
        return self._price_unit

    @property
    def recording_sid(self):
        """ The recording_sid """
        return self._recording_sid

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def status(self):
        """ The status """
        return self._status

    @property
    def transcription_text(self):
        """ The transcription_text """
        return self._transcription_text

    @property
    def type(self):
        """ The type """
        return self._type

    @property
    def uri(self):
        """ The uri """
        return self._uri

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
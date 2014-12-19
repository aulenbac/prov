__author__ = 'Trung Dong Huynh'
__email__ = 'trungdong@donggiang.com'

import logging
logger = logging.getLogger(__name__)

from prov.serializers import Serializer


class ProvNSerializer(Serializer):
    """PROV-N serializer for ProvDocument

    """
    def serialize(self, stream, **kwargs):
        """
        Serializes a :class:`prov.model.ProvDocument` instance to a
        `PROV-N <http://www.w3.org/TR/prov-n/>`_.

        :param stream: Where to save the output.
        """
        provn_content = self.document.get_provn()
        stream.write(provn_content.encode('utf-8'))

    def deserialize(self, stream, **kwargs):
        raise NotImplemented
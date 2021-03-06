#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import (
    TApplicationException,
    TMessageType,
    TProcessor,
    TType,
)
from thrift.transport import TTransport

from opencensus.ext.jaeger.trace_exporter.gen.jaeger import jaeger


class Iface(object):
    def emitBatch(self, batch):
        """
        Parameters:
         - batch
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def emitBatch(self, batch):
        """
        Parameters:
         - batch
        """
        self.send_emitBatch(batch)

    def send_emitBatch(self, batch):
        self._oprot.writeMessageBegin('emitBatch', TMessageType.ONEWAY,
                                      self._seqid)
        args = emitBatch_args()
        args.batch = batch
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["emitBatch"] = Processor.process_emitBatch

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD,
                                      'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_emitBatch(self, seqid, iprot, oprot):
        args = emitBatch_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.emitBatch(args.batch)
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise


# HELPER FUNCTIONS AND STRUCTURES


class emitBatch_args(object):
    """
    Attributes:
     - batch
    """

    thrift_spec = (
        None,  # 0
        (
            1,
            TType.STRUCT,
            'batch',
            (jaeger.Batch, jaeger.Batch.thrift_spec),
            None,
        ),  # 1
    )

    def __init__(
            self,
            batch=None,
    ):
        self.batch = batch

    def read(self, iprot):
        if iprot._fast_decode is not None and \
                isinstance(iprot.trans, TTransport.CReadableTransport) and \
                self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.batch = jaeger.Batch()
                    self.batch.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('emitBatch_args')
        if self.batch is not None:
            oprot.writeFieldBegin('batch', TType.STRUCT, 1)
            self.batch.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
                                self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

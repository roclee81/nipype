# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import MRIsInflate


def test_MRIsInflate_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=True,
    mandatory=True,
    position=-2,
    ),
    no_save_sulc=dict(argstr='-no-save-sulc',
    xor=['out_sulc'],
    ),
    out_file=dict(argstr='%s',
    hash_files=False,
    keep_extension=True,
    name_source=['in_file'],
    name_template='%s.inflated',
    position=-1,
    ),
    out_sulc=dict(xor=['no_save_sulc'],
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = MRIsInflate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRIsInflate_outputs():
    output_map = dict(out_file=dict(),
    out_sulc=dict(),
    )
    outputs = MRIsInflate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

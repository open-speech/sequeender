// sequeender/py/cc/sequeender.cc

// Copyright (c)  2020  Fangjun Kuang (csukuangfj@gmail.com)

// See ../../../LICENSE for clarification regarding multiple authors

#include "sequeender/py/cc/sequeender.h"

#include "sequeender/py/cc/array.h"
#include "sequeender/py/cc/fsa.h"
#include "sequeender/py/cc/fsa_util.h"

PYBIND11_MODULE(_sequeender, m) {
  m.doc() = "pybind11 binding of sequeender";
  PybindArc(m);
  PybindArray(m);
  PybindFsa(m);
  PybindFsaUtil(m);
}

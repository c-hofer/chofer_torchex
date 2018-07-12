#pragma once

#include <ATen/ATen.h>

using namespace at;

namespace CalcPersCuda
{

Tensor find_merge_pairings(
    const Tensor & pivots,
    int64_t max_pairs = -1);

void merge_columns(
    Tensor & compr_desc_sort_ba,
    const Tensor & merge_pairs);

std::vector<std::vector<Tensor>> read_barcodes(
    const Tensor & pivots,
    Tensor & simplex_dimension,
    int64_t max_dimension);

std::vector<std::vector<Tensor>> calculate_persistence(
    Tensor &  compr_desc_sort_ba,
    Tensor & ba_row_i_to_bm_col_i,
    Tensor & simplex_dimension,
    int64_t max_dimension,
    int64_t max_pairs);

Tensor my_test_f(Tensor t);

} // namespace CalcPersCuda
function customSort(sortName, sortOrder, data) {
    var order = sortOrder === 'desc' ? -1 : 1
    data.sort(function (a, b) {
      var aa = +((a[sortName] + '').replace(/[^\d]/g, ''))
      var bb = +((b[sortName] + '').replace(/[^\d]/g, ''))
      if (aa < bb) {
        return order * -1
      }
      if (aa > bb) {
        return order
      }
      return 0
    })
  }
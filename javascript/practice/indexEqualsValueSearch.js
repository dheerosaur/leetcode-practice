  let mid = 0,
    left = 0,
    right = arr.length;

  while (left < right) {
    if (arr[mid] >= mid) {
      right = mid;
    } else {
      left = mid + 1;
    }
    mid = Math.floor((left + right) / 2);
  }
  if (arr[mid] === mid) return mid;
  return -1;
}

console.log(indexEqualsValueSearch([0]));
console.log(indexEqualsValueSearch([-9, 0, 2, 5]));
console.log(indexEqualsValueSearch([-1, 0, 1, 2, 3, 4, 6]));
console.log(indexEqualsValueSearch([-1, 0, 3, 6]));

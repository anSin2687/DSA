class MajorityElement():
  def majority(A,N):
    hist = {}
    for element in A:
      if element in hist.keys():
        hist[element] += 1
      elif element not in hist.keys():
        hist[element] = 1
      if hist[element] > N/2:
        return element
      
    return -1


if __name__ == "__main__":
  A = [1,2,3,5,3,5,3,3,3]
  major = MajorityElement.majority(A,len(A))
  print(major)

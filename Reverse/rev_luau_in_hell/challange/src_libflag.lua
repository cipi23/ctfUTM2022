local function _checkFlag(_flag, _key)
    local ans = {40, 51, 35, 114, 60, 50, 127, 6, 111, 2, 65, 57, 96, 18, 48, 101, 25, 20, 71, 92, 73, 116, 1, 23, 0, 23, 1}
    if #_flag ~= #ans then
       return false
    end
 
    local flag = {}
    local key = {}
    for i = 1, #_flag do
       flag[i] = string.byte(_flag:sub(i, i+1))
    end
    for i = 1, #_key do
       key[i] = string.byte(_key:sub(i, i+1))
    end
 
    for i = 1, #flag do
       for j = i + 1, #flag do
          local t = flag[i]
          flag[i] = flag[j]
          flag[j] = t
       end
    end
 
    for i = 1, #flag do
       flag[i] = flag[i] ~ key[1 + ((i-1) % #key)]
       if flag[i] ~= ans[i] then
          return false
       end
    end
 
    return true
 end
 
 return {
    checkFlag = _checkFlag
 }
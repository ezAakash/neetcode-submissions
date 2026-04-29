class Solution {

    public String encode(List<String> strs) {
        StringBuilder s = new StringBuilder();
        for(String e: strs){
            s.append(e).append('.');
        }

        return new String(s);
    }

    public List<String> decode(String str) {
        char[] ch = str.toCharArray();
        List<String> dec = new ArrayList<>();
        StringBuilder s = new StringBuilder();
        for(char c: ch){
            if(c == '.'){
                dec.add(new String(s));
                s.setLength(0);
                continue;
            }
            s.append(c);
        }

        return dec;
    }
}

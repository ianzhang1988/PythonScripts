class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_list = [int(i) for i in num1]
        num2_list = [int(i) for i in num2]
        
        # print(num1_list, num2_list)
        
        num1_list.reverse()
        num2_list.reverse()
        
        #print(num1_list, num2_list)
        
        product = [0 for _ in range(len(num1_list)+len(num2_list))]
        
        for idx1, val1 in enumerate(num1_list):
            # if val1 == 0:
            #     continue
            for idx2, val2 in enumerate(num2_list):
                # if val2 == 0:
                #     continue
                sub_product = val1*val2
                with_previous_val = sub_product+product[idx1+idx2]
                jinwei = with_previous_val//10
                remained = with_previous_val%10
                product[idx1+idx2] = remained
                product[idx1+idx2+1] += jinwei
        
        #print(product)
        
        product.reverse()

        for idx, i in enumerate(product):
            if i > 0:
                break
        
        product_trim = product[idx:]
        product_trim = [str(i) for i in product_trim]
        product_str = ''.join(product_trim)

        #print(product_str)
        
        return product_str

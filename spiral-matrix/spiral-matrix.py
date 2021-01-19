class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        down = len(matrix)-1
        right = len(matrix[0])-1  #columnss
        left = 0
        direction = 0 #0: l_r, 1: t_b, 2:r_l, 3:b_u 
        ans = []
        while left <= right and top <= down:
            
            if direction ==0: #left_right
                for i in range(left,right+1):
                    ans.append(matrix[top][i])                    
                top+=1
                
            elif direction ==1: #top_down
                for i in range(top,down+1):
                    ans.append(matrix[i][right])
                right-=1
                
            elif direction == 2: #right_left
                for i in reversed(range(left,right+1)):
                    ans.append(matrix[down][i])
                down-=1
                
            elif direction == 3: #bottom_top
                for i in reversed(range(top,down+1)):
                    ans.append(matrix[i][left])
                left+=1
            direction = (direction + 1) % 4
            
        return ans
                
​
        

# import torchvision.models as models
# models.resnet34(pretrained=True)


import cv2


'''
model(对象).train()# ：启用 BatchNormalization 和 Dropout
model(对象).eval() ：不启用 BatchNormalization 和 Dropout
'''
# print(100//11)
##############################################################################################################################
# import cv2
# # 采用opencv的库函数去调用摄像头
#
# cap = cv2.VideoCapture(0)
# # cv2.VideoCapture(0)代表调取摄像头资源，其中0代表电脑摄像头，1代表外接摄像头(usb摄像头)
#
# cap.set(3, 900)
# cap.set(4, 900)
# # cap.set（）设置摄像头参数：3:宽   4:高
#
# while True:
#   ret, frame = cap.read()       # 读摄像头
#   cv2.imshow("video", frame)
#   if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
#     break

##############################################################################################################################

# p=[1] * 5  #
# print(p)  #[1, 1, 1, 1, 1]

##############################################################################################################################


# p=[1,6,8,1,3,1,8,4,2,3,1,3,9,8,6,4,6,9,4]
#
# print(p.index(1))  #重复的元素只输出第一个元素的序号

##############################################################################################################################


# dict={'1':1,"2":2}
#
# if '1' not in dict:
#     print(0)
#
# else:
#     print(1)

##############################################################################################################################
# n=int(input())
# print(n)
# machine=""
# while n>0:
#     if n%2==0:
#         machine="2"+machine
#         n=n/2-1
#     else:
#         machine="1"+machine
#         n=(n-1)/2
# for i in machine:
#     print(i)

##############################################################################################################################
# -*- coding: utf-8 -*-

# from sklearn.preprocessing import  OneHotEncoder
#
# enc = OneHotEncoder(sparse = False)
# ans = enc.fit_transform([[0, 0, 3],
#                          [1, 1, 0],
#                          [0, 2, 1],
#                          [1, 0, 2]])   #第一列两个特征N=2 第二列三个特征N=3 第三列四个特征N=4 (——，——|，——，——，——|,——，——，——，——)所以每一行的形状就是这样，除非要转换的数据超过N
#
# print(ans) # 输出 [[ 1.  0.  1. ...,  0.  0.  1.]
           #      [ 0.  1.  0. ...,  0.  0.  0.]
           #      [ 1.  0.  0. ...,  1.  0.  0.]
           #      [ 0.  1.  1. ...,  0.  1.  0.]]


##############################################################################################################################

# list_all=[]
#
# n_list=int(input())
# for j in range(n_list):
#     list_len=int(input())
#     list_str=input().split(' ')
#     for i  in range(list_len):
#         listi = [int(list_str[i]) for i in range(list_len)]
#
#     list_all.append(listi)
#
# print(list_all)
##############################################################################################################################

'''
list的最大值max获取：
'''
# list1=["1","2","3","4"]
# # print(list1[0][1])
#
#
# # check=
#
# maxgrade=max(list1[1:3])
#
# print(maxgrade)

##############################################################################################################################

# 字符串可以切片
# str="like.o\o"
#
# print((str[0:2]))


# list1=[[1, 2, 3 ,4],[2 ,6, 4 ,5]]
# print(list1[1])
# print(len(list1))
##############################################################################################################################

# class tree():
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None
#
# t1=tree(1)
# t2=tree(2)
# t3=tree(3)
# t4=tree(4)
# t5=tree(5)
# t6=tree(6)
# t7=tree(7)
# # t8=tree(8)
#
# #构造树结构
# t1.left=t2
# t1.right=t3
# t2.left=t4
# t2.right=t5
# t3.left=t6
# t3.right=t7
# # t6.right=t8
#
# treelist = []
# def midsort(root):
#
#     if root == None: return None
#
#     midsort(root.left)
#     treelist.append(root.val)
#     midsort(root.right)
#
#     return treelist
#
# print(midsort(t1))

##############################################################################################################################

# list1=[1,2,3]
# list2=list1[:]+[4]
# print(list2)


#读取txt文件信息
# imagesetfile='/home/lijunyu/codes/darknet/data/ImageSets/Main/test.txt'
# img=[]
# for x in open(imagesetfile):
#     img.append(x.split('\n')[0])
# # img=[x.strip() for x in imagesetfile]
# print(img)


##############################################################################################################################


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         if len(nums1) + len(nums2) == 0:
#             return 0
#
#         s1 = 0
#         s2 = 0
#         mid1 = 0
#         mid2 = 0
#         for i in range((len(nums1) + len(nums2)) // 2 + 1):
#             if s1 > (len(nums1) - 1):
#                 mid1 = mid2
#                 mid2 = nums2[s2]
#                 s2 += 1
#                 continue
#             if s2 > (len(nums2) - 1):
#                 mid1 = mid2
#                 mid2 = nums1[s1]
#                 s1 += 1
#                 continue
#             if nums2[s2] > nums1[s1]:
#                 mid1 = mid2
#                 mid2 = nums1[s1]
#                 s1 += 1
#             else:
#                 mid1 = mid2
#                 mid2 = nums2[s2]
#                 s2 += 1
#
#         if (len(nums1) + len(nums2)) % 2 != 0:  # 奇数个数，找中间那个
#             return mid2
#         else:
#             return (mid1 + mid2) / 2.0
#
#
#
#
#
# list1=[1,2]
# list2=[3,4]
# S=Solution()
# print(S.findMedianSortedArrays(list1,list2))



###############################################################3###############################################################3

###############################################################3###############################################################3###############################################################3


#将列表中的字符全部转换成int       利用map

# l1=[['1', '4', '9'], ['3', '5', '9']]
# l2=[]
# for i in range(len(l1)):
#     l2.append(list(map(int, l1[i])))
#
# print(l2)

###############################################################3###############################################################3###############################################################3

# import numpy as np
# th=0.35
#
# ori=np.array([0.6,0.1,0.65,0.3])
# p=np.where(ori<=th)[0]  ####################   np.where返回数组满足条件的项
#
# axis=np.array([0,1,2,3])
#
# out=axis[p]  #可以array1[array2]使用，返回array1中序号为array2的项
# print(p,type(p))
# print(out)

###############################################################3###############################################################3###############################################################3


# list1=[[1,2],[2,3],[3,4]]
#
# for i,j in list1:
#     print(i,j)
# print("#"*20)
# p = [[] for i in range(len(list1)+1)]
#
# print(p)
#
#
# 4
# 5 3 7
# 2 8 14 15 17 23 29
# 5 3 6
# 2 8 14 17 23 29
# 5 2 2
# 3 7
# 5 2 2
# 3 8


# n=int(input())
# list_rule=[]
# list_wrong=[]
# for i in range(n):
#     ru=input().split(' ')
#     wr=input().split(' ')
#
#     list_rule.append(list(map(int,ru)))
#     list_wrong.append(list(map(int,wr)))
#
# for i in range(n):
#     A_N=[list_wrong[i][0]]#记录小于间隔小于5的时间
#
#     wrong = list_wrong[i]
#
#     A = list_rule[i][0]
#     B = list_rule[i][1]
#     nN=list_rule[i][2]
#
#
#     for n in range(1,nN):
#         if wrong[n]-A_N[0]<5:
#             A_N.append(wrong[n])
#
#             if len(A_N)>=B:
#                 print("Yes")
#                 break
#         else:
#             while len(A_N)!=0 and wrong[n]-A_N[0]>=5:
#                 del A_N[0]
#             A_N.append(wrong[n])
#     if len(A_N)<B:
#         print("No")


#深信服
# 1.#######################3
# 4
# 5 3 7
# 2 8 14 15 17 23 29
# 5 3 6
# 2 8 14 17 23 29
# 5 2 2
# 3 7
# 5 2 2
# 3 8

# Yes
# No
# Yes
# No

# 2.#######################
# 2
# 3
# 2 1 3
# 3
# 1 2 3

# 2
# 3

# 3.#######################
# 4
# 1 5
# 1 2 3 4 5
# 2 5
# 1 2 3 4 5
# 5 4 3 2 1
# 3 5
# 1 2 3 4 5
# 1 3 5 2 4
# 3 4 2 1 5
# 2 5
# 1 2 5 4 3
# 5 2 1 4 3

# 16
# 2
# 0
# 8
###############################




# print(list_rule)
# print(list_wrong)


class Solution:
    def rightSideView(self, root) :
        if root == None:
            return []

        # level=collections.deque()
        level = [root]
        right_path = []

        while level:
            right_node = level[0]
            right_path.append(right_node.val)
            length_level = len(level)
            for i in range(length_level):
                cur_node = level[0]
                if cur_node.right:
                    level.append(cur_node.right)
                if cur_node.left:
                    level.append(cur_node.right)
                del level[0]

        return right_path








  '''                          if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                                print parent.state[cnt1-2][cnt2-2],cnt1-2,cnt2-2
                                if (list(parent.state[cnt1-1][cnt2-1])[0] == 'C'):
                                    #recursive call and move to this position
                                    print "pri3"
                                    temp_state = copy.deepcopy(parent.state)
                                    #check for super-imposing moves on the last node
                                    if (temp_state[cnt1-2][cnt2-2] != '0') and (cnt1-2 == 0):
                                        last_row_cond = int(list(temp_state[cnt1-2][cnt2-2])[1])
                                        last_row_cond += 1
                                        temp_state[cnt1-2][cnt2-2] = "S" + str(last_row_cond)
                                    else:
                                        temp_state[cnt1-2][cnt2-2] = 'S1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1-1][cnt2-1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    print "------------------------------------------------------------"
                                    depth_cntr-=1
                                    if depth_cntr < 0:
                                        return
                                    else:
                                        self.move_generation(depth_cntr,temp_node)
                                else:
                                    #skip
                                    print "pri33"
                                
                            if ((cnt1-2 >=0 and cnt1-2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                                print parent.state[cnt1-2][cnt2+2],cnt1-2,cnt2+2
                                if ((parent.state[cnt1-2][cnt2+2] == '0') and (list(parent.state[cnt1-1][cnt2+1])[0] == 'C')):
                                    #recursive call and move to this position
                                    print "pri4"
                                    temp_state = copy.deepcopy(parent.state)
                                    temp_state[cnt1-2][cnt2+2] = 'S1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1-1][cnt2+1] = '0'
                                    temp_node = Node(0, temp_state, parent)
                                    print "------------------------------------------------------------"
                                    depth_cntr-=1
                                    if depth_cntr < 0:
                                        return
                                    else:
                                        self.move_generation(depth_cntr,temp_node)
                                else:
                                    #skip 
                                    print "pri44"  '''










 '''                           if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2-2 >=0 and cnt2-2 <= 7)):
                                print parent.state[cnt1+2][cnt2-2],cnt1-2,cnt2-2
                                if ((parent.state[cnt1+2][cnt2-2] == '0') and (list(parent.state[cnt1+1][cnt2-1])[0] == 'S')):
                                    #recursive call and move to this position
                                    print "pri3"
                                    temp_state = copy.deepcopy(parent.state)
                                    temp_state[cnt1+2][cnt2-2] = 'C1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1+1][cnt2-1] = '0'
                                    temp_node = Node(1, temp_state, parent)
                                    print "------------------------------------------------------------"
                                    depth_cntr-=1
                                    if depth_cntr < 0:
                                        return
                                    else:
                                        self.move_generation(depth_cntr,temp_node)
                                else:
                                    #skip
                                    print "pri33"
                                
                            if ((cnt1+2 >=0 and cnt1+2 <= 7) and (cnt2+2 >=0 and cnt2+2 <= 7)):
                                print parent.state[cnt1+2][cnt2+2],cnt1-2,cnt2+2
                                if ((parent.state[cnt1+2][cnt2+2] == '0') and (list(parent.state[cnt1+1][cnt2+1])[0] == 'S')):
                                    #recursive call and move to this position
                                    print "pri4"
                                    temp_state = copy.deepcopy(parent.state)
                                    temp_state[cnt1+2][cnt2+2] = 'C1'
                                    temp_state[cnt1][cnt2] = '0'
                                    temp_state[cnt1+1][cnt2+1] = '0'
                                    temp_node = Node(1, temp_state, parent)
                                    print "------------------------------------------------------------"
                                    depth_cntr-=1
                                    if depth_cntr < 0:
                                        return
                                    else:
                                        self.move_generation(depth_cntr,temp_node)
                                else:
                                    #skip 
                                    print "pri44"'''
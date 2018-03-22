# pygame--
python最小游戏框架
屏幕绘制的重要函数
——1.屏幕尺寸和模式
     pygame.display.set_mode(size,flags)设置相关屏幕模式
          flags用于显示类型，可组合使用，常用显示标签如下：
               pygame.RESIZABLE 窗口大小可调
               pygame.NOFRAM    窗口没有边界显示
               pygame.FULLSCREEN窗口全屏显示
     pygame.display.Info()生成屏幕相关信息
——2.窗口标题和图表
     pygame.display.set_caption()设置标题信息
     pygame.display.set_icon()设置图标信息
     pygame.display.get_cation()获得图标
——3.窗口感知和图表
     pygame.display.get_active()
     pygame.display.flip()
     pygame.display.update()

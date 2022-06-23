### 모델 과적합 발생 회피
seed = 0
np.random.seed(seed)
tf.compat.v1.set_random_seed(seed)

model = Sequential()
model.add(Dense(units = 30, input_dim = 12, activation = 'relu'))
model.add(Dense(units = 12, activation = 'relu'))
model.add(Dense(units = 8, activation = 'relu'))
model.add(Dense(units = 1,  activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', 
              optimizer = 'adam', metrics = ['accuracy'])

# 모델 저장 폴더 설정
MODEL_DIR = 'C:/Users/user/ICTIS_2022_1/WineModel'
if not os.path.exists(MODEL_DIR): # 디렉토리가 없으면 폴더 생성
    os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelfile = MODEL_DIR + '/wine_best.h5'
# save_best_onl : best일 때만 저장(전보다 loss가 줄어드는 epoch 저장)
checkpointer = ModelCheckpoint(filepath = modelfile,
                              monitor = 'val_loss', verbose = 0,
                              save_best_only = True)

# 학습의 자동 중단 설정
# patience : 값이 튀는 부분이 나왔을 때 참고 몇 번 넘어간 후에 과적합 결정할지
early_stopping_callback = EarlyStopping(monitor = 'val_loss',
                                       patience = 1000)

# 모델 학습 및 저장
# batch size 크면, 속도 빨라지면서 weight를 rough하게 변화시킴
fit_history = model.fit(X, Y, epochs = 35000, batch_size = 500,
                       validation_split = 0.33, verbose = 0, 
                       callbacks = [early_stopping_callback, checkpointer])

print('Accuracy: %.4f' % (model.evaluate(X, Y)[1]))


### loss 그래프
vloss = fit_history.history['val_loss'] # Test set loss
loss = fit_history.history['loss'] # Train set loss

plt.figure(figsize = (12, 5))
epoch = np.arange(len(loss))
plt.plot(epoch, vloss, 'r', label = 'validation_loss')
plt.plot(epoch, loss, 'b', label = 'loss')
plt.legend(loc = 'best')
plt.show()


### accuarcy 그래프
vacc = fit_history.history['val_accuracy'] # Test set loss
acc = fit_history.history['accuracy'] # Train set loss

plt.figure(figsize = (12, 5))
epoch = np.arange(len(acc))
plt.plot(epoch, vacc, 'r', label = 'validation_acc')
plt.plot(epoch, acc, 'b', label = 'accuracy')
plt.legend(loc = 'best')
plt.show()


### 저장한 모델 로드
from tensorflow.keras.models import load_model

optimal_model = load_model('C:/Users/user/ICTIS_2022_1/WineModel/wine_best.h5')
# 모든 데이터셋으로 평가하였으므로, optimal_model의 성능이 약간 낮게 나옴
# 그러나 Test set에 대한 성능은 과적합된 모델보다 더 좋다
print('Accuracy: %.4f' % (model.evaluate(X, Y)[1]))
